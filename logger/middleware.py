import threading
from logging import getLogger, config
from typing import Optional, Dict

from rest_framework import status
from django.utils.deprecation import MiddlewareMixin

from .dict_loggers import django_logging

config.dictConfig(django_logging)


class LoggerMiddleware(MiddlewareMixin):
    logger = getLogger('logger')
    error_name = None
    mutex = threading.Lock()

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
        getattr(self.logger, level)(msg, extra=kwargs)

    def process_response(self, request, response):
        request_data = LoggerMiddleware.get_request_data(request)
        base_data = {"status_code": response.status_code, "url": request.path, "method": request.method,
                     "request_data": request_data, "response_data": getattr(response, "data", None),
                     "error_name": None,
                     "module_name": getattr(getattr(request.resolver_match, "func", None), "__name__",
                                            None)}

        if status.is_server_error(response.status_code):
            self.doing_log('critical', response.reason_phrase,
                           **base_data | {"error_name": self.error_name})
            self.mutex.release()

        if status.is_client_error(response.status_code):
            self.doing_log('error', response.reason_phrase,
                           **base_data)

        if status.is_success(response.status_code) or status.is_redirect(response.status_code):
            self.doing_log('info', response.reason_phrase,
                           **base_data)
        return response

    def process_exception(self, request, exception):
        self.mutex.acquire()
        self.error_name = f"{type(exception).__name__}: {str(exception)}"
        return None
