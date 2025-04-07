from pythonjsonlogger.jsonlogger import JsonFormatter
from jdatetime import datetime
from logging import Formatter


class JalaliFormatter(Formatter):
    def formatTime(self, record, datefmt=None):
        return datetime.now().strftime('%Y/%m/%d %H:%M:%S')


class JalaliJsonFormatter(JsonFormatter):
    def formatTime(self, record, datefmt=None):
        return datetime.now().strftime('%Y/%m/%d %H:%M:%S')


formatter = {
    'standard': {
        '()': 'django-logger.logger_formatter.JalaliFormatter',
        'format': '\nlogged:\n\t{message} - {status_code} - {url} - {method}\n\tuser: {user}\n\trequest data: {request_data}\n\tresponse data: {response_data}\n\terror: {error_name}\n\t{asctime} - {levelname} - {module_name}\n',
        'style': '{',
    },
    'json': {
        '()': 'django-logger.logger_formatter.JalaliJsonFormatter',
        'fmt': '{message} - {status_code} - {url} - {method} - {user} - {request_data} - {response_data} - {error_name} - {asctime} - {levelname} - {module_name}',
        'style': '{'
    },
}
