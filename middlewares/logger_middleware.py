from rest_framework import status
from logging import handlers, Filter, getLogger
from pathlib import Path
from datetime import datetime


class RotationFileHandler(handlers.RotatingFileHandler):
    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False):
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        super().__init__(filename, mode, maxBytes, backupCount, encoding, delay)


class LevelFilter(Filter):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelname == self.level


filters = {
    'info_filter': {
        '()': LevelFilter,
        'level': 'INFO',
    },
    'warning_filter': {
        '()': LevelFilter,
        'level': 'WARNING',
    },
    'error_filter': {
        '()': LevelFilter,
        'level': 'ERROR',
    },
    'critical_filter': {
        '()': LevelFilter,
        'level': 'CRITICAL',
    },
}

formatter = {
    'standard': {
        'format': '{message} - {status_code} - {url} - {method}\n{request_data}\n{response_data}\n{error_name}\n{asctime} - {levelname} - {filename} - {lineno} - {module}',
        'style': '{',
    },
    'json': {
        '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
        'fmt': '{message} - {status_code} - {url} - {method}\n{request_data}\n{response_data}\n{error_name}\n{asctime} - {levelname} - {filename} - {lineno} - {module}',
        'style': '{'
    },
}

base_rotating_handler = {
    'class': RotationFileHandler,
    'maxBytes': 10 * (2 ** 20),
    'backupCount': 5,
    'encoding': 'UTF-8',
    'formatter': 'json',
}

handlers = {
    'console': {
        'class': 'logging.StreamHandler',
        'formatter': 'standard',
    },
    'rotating_file_handler_info': {
        **base_rotating_handler,
        'filename': f'logs/{datetime.today().strftime('%Y-%m-%d')}/INFO.log',
        'filters': ['info_filter'],
    },
    'rotating_file_handler_warning': {
        **base_rotating_handler,
        'filename': f'logs/{datetime.today().strftime('%Y-%m-%d')}/WARNING.log',
        'filters': ['warning_filter'],
    },
    'rotating_file_handler_error': {
        **base_rotating_handler,
        'filename': f'logs/{datetime.today().strftime('%Y-%m-%d')}/ERROR.log',
        'filters': ['error_filter'],
    },
    'rotating_file_handler_critical': {
        **base_rotating_handler,
        'filename': f'logs/{datetime.today().strftime('%Y-%m-%d')}/CRITICAL.log',
        'filters': ['critical_filter'],
    },
}

loggers = {
    'd': {
        'handlers': ['console', 'rotating_file_handler_info', 'rotating_file_handler_warning',
                     'rotating_file_handler_error', 'rotating_file_handler_critical'],
        'level': 'INFO',
        'propagate': False,
    },
}

django_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': filters,
    'formatters': formatter,
    'handlers': handlers,
    'loggers': loggers,
}


def find_status_name(code):
    return [name_status.split("_")[-1] for name_status in dir(status) if name_status.startswith("HTTP_" + str(code))][0]


from django.utils.deprecation import MiddlewareMixin


class LoggerMiddleware(MiddlewareMixin):
    logger = getLogger('d')

    def process_response(self, request, response):
        if status.is_success(response.status_code):
            self.logger.info(find_status_name(response.status_code),
                             extra={"status_code": response.status_code, "url": request.path, "method": request.method,
                                    "request_data": request.body, "response_data": response.data, "error_name": None})
        if status.is_redirect(response.status_code):
            self.logger.warning(find_status_name(response.status_code),
                                {"status_code": response.status_code, "response_data": response.data})
        if status.is_client_error(response.status_code):
            self.logger.error(find_status_name(response.status_code),
                              {"status_code": response.status_code,
                               "response_data": response.data if hasattr(response, "data") else None})
        if status.is_server_error(response.status_code):
            self.logger.critical(find_status_name(response.status_code),
                                 {"status_code": response.status_code,
                                  "response_data": response.data if hasattr(response, "data") else None})
        print("hello")
        return response

    # def process_exception(self, request, exception):
    #     critical(find_status_name(500), exception)
    #     return None
