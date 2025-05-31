from logging import handlers
from pathlib import Path

from django.conf import settings

log_data = getattr(settings, 'LOG_DATA', {})

log_path = log_data.get('LOG_PATH')

if log_path is None:
    raise ValueError('LOG_PATH should not be empty')

backup_counts = log_data.get('BACKUP_COUNTS', {})

backup_count_info = backup_counts.get('BACKUP_COUNT_INFO', 0)
backup_count_error = backup_counts.get('BACKUP_COUNT_ERROR', 10)
backup_count_critical = backup_counts.get('BACKUP_COUNT_CRITICAL', 100)

max_bytes = log_data.get('MAX_BYTES', {})

max_bytes_info = max_bytes.get('MAX_BYTES_INFO', 2 ** 20)
max_bytes_error = max_bytes.get('MAX_BYTES_ERROR', 2 ** 20)
max_bytes_critical = max_bytes.get('MAX_BYTES_CRITICAL', 10 * (2 ** 20))

encoding = log_data.get('LOG_ENCODING', 'UTF-32')


class RotationFileHandler(handlers.RotatingFileHandler):
    def __init__(self, filename, mode='a', max_bytes=0, backup_count=0, encoding=None, delay=False):
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        super().__init__(filename, mode, max_bytes, backup_count, encoding, delay)


base_rotating_handler = {
    'class': 'django_logger.logger_handlers.RotationFileHandler',
    'encoding': encoding,
    'formatter': 'json',
}

handlers = {
    'console': {
        'class': 'logging.StreamHandler',
        'formatter': 'standard',
    },
    'rotating_file_handler_info': {
        **base_rotating_handler,
        'max_bytes': max_bytes_info,
        'backup_count': backup_count_info,
        'filename': f'{log_path}/Information/INFO.log',
        'filters': ['info_filter'],
    },
    'rotating_file_handler_error': {
        **base_rotating_handler,
        'max_bytes': max_bytes_error,
        'backup_count': backup_count_error,
        'filename': f'{log_path}/Errors/ERROR.log',
        'filters': ['error_filter'],
    },
    'rotating_file_handler_critical': {
        **base_rotating_handler,
        'max_bytes': max_bytes_critical,
        'backup_count': backup_count_critical,
        'filename': f'{log_path}/Critical/CRITICAL.log',
        'filters': ['critical_filter'],
    },
}
