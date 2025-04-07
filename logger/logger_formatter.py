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
        '()': JalaliFormatter,
        'format': '\nlogged:\n\t{message} - {status_code} - {url} - {method}\n\t{request_data}\n\t{response_data}\n\t{error_name}\n\t{asctime} - {levelname} - {module_name}\n',
        'style': '{',
    },
    'json': {
        '()': JalaliJsonFormatter,
        'fmt': '{message} - {status_code} - {url} - {method} - {request_data} - {response_data} - {error_name} - {asctime} - {levelname} - {module_name}',
        'style': '{'
    },
}
