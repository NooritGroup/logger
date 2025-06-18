from pythonjsonlogger.jsonlogger import JsonFormatter
from jdatetime import datetime
from logging import Formatter


class JalaliFormatter(Formatter):
    def formatTime(self, record, datefmt=None):
        return datetime.now().strftime('%Y/%-m/%-d %-H:%-M:%-S.%f %A')


class JalaliJsonFormatter(JsonFormatter):
    def formatTime(self, record, datefmt=None):
        return datetime.now().strftime('%Y/%-m/%-d %-H:%-M:%-S.%f %A')


formatter = {
    'standard': {
        '()': 'django_logger.logger_formatter.JalaliFormatter',
        'format': (
            '\nlogged:\n\t{message} - {status_code} - {url} - {path} - {method}\n\t'
            'user: {user}\n\tIP: {IP}\n\tSession Id: {session_id}\n\tProtocol: {Protocol}\n\t'
            'request data: {request_data}\n\tresponse data: {response_data}\n\t'
            'Sec Ch Ua Platform: {sec_ch_ua_platform}\n\tUser Agent: {user_agent}\n\t'
            'Accept Encoding: {accept_encoding}\n\tCsrf Token: {csrf_token}\n\t'
            'error: {error_name}\n\t{asctime} - {levelname} - {module_name}\n'
        ),
        'style': '{',
    },
    'json': {
        '()': 'django_logger.logger_formatter.JalaliJsonFormatter',
        'fmt': (
            '{message} - {status_code} - {url} - {path} - {method} - '
            '{user} - {IP} - {session_id} - {Protocol} - '
            '{request_data} - {response_data} - '
            '{sec_ch_ua_platform} - {user_agent} - '
            '{accept_encoding} - {csrf_token} - '
            '{error_name} - {asctime} - {levelname} - {module_name}'
        ),
        'style': '{'
    },
}
