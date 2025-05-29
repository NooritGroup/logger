import traceback
import re
from logging import getLogger, config
from typing import Optional, Dict

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from rest_framework import status

from .dict_loggers import django_logger

config.dictConfig(django_logger)


def mask_sensitive_data(data, mask_api_parameters=False, parameters=None):
    """
    Masks or removes sensitive data such as passwords or tokens from dictionaries or URL strings.

    Parameters:
    -----------
    data : dict, str, list
        The input data to be cleaned. Can be a dictionary, list of dicts, or URL string.
    mask_api_parameters : bool
        If True, applies masking to query parameters in a string (URL format).
        Otherwise, it recursively filters keys from dictionaries/lists.

    Returns:
    --------
    dict, str, list
        The sanitized version of the input data, with sensitive values replaced by "***FILTERED***".
    """
    if parameters is None:
        parameters = ['password', 'token', 'access', 'refresh']
    if type(data) is not dict:
        # Handle query string case if enabled
        if mask_api_parameters and type(data) is str:
            for sensitive_key in parameters:
                # Replaces values like token=abcd1234& -> token=***FILTERED***&
                data = re.sub(
                    '({}=)(.*?)($|&)'.format(sensitive_key),
                    r'\1***FILTERED***\3',
                    data
                )

        # If it's a list, sanitize each item recursively
        if type(data) is list:
            data = [mask_sensitive_data(item) for item in data]
        return data

    # Process each key-value pair in the dictionary
    for key, value in data.items():
        if key in parameters:
            data[key] = "***FILTERED***"  # Mask sensitive keys

        elif type(value) is dict:
            data[key] = mask_sensitive_data(data[key])  # Recurse into nested dict

        elif type(value) is list:
            data[key] = [mask_sensitive_data(item) for item in data[key]]  # Recurse into list

    return data


class LoggerMiddleware(MiddlewareMixin):
    logger = getLogger('django-logger')
    error_name = None

    @staticmethod
    def get_request_data(request) -> Optional[Dict]:
        if request.method == 'DELETE':
            return None
        elif request.method in ('PUT', 'PATCH'):
            request_data = request.POST.dict()
        else:
            request_data = getattr(request, request.method).dict()
        return request_data | request.FILES.dict()

    def doing_log(self, level, msg, **kwargs) -> None:
        getattr(self.logger, level)(msg, extra=mask_sensitive_data(kwargs, mask_api_parameters=True))

    def process_response(self, request, response):
        request_data = LoggerMiddleware.get_request_data(request)
        path_file = getattr(getattr(request.resolver_match, "func", None), "__module__", None)
        base_data = {"status_code": response.status_code, "url": request.path, "method": request.method,
                     "user": request.user,
                     "request_data": request_data, "response_data": getattr(response, "data", None),
                     "error_name": None,
                     "module_name": path_file.replace('\\', '/')
                     .replace(str(settings.BASE_DIR).replace('\\', '/'), '') if path_file else None}

        if status.is_server_error(response.status_code):
            self.doing_log('critical', response.reason_phrase,
                           **base_data | {"error_name": self.error_name})

        if status.is_client_error(response.status_code):
            self.doing_log('error', response.reason_phrase,
                           **base_data)

        if status.is_success(response.status_code) or status.is_redirect(response.status_code):
            self.doing_log('info', response.reason_phrase,
                           **base_data)
        return response

    def process_exception(self, request, exception):
        self.error_name = traceback.format_exc()
        return None
