from logging import handlers
from pathlib import Path


class RotationFileHandler(handlers.RotatingFileHandler):
    def __init__(self, filename, mode='a', max_bytes=0, backup_count=0, encoding=None, delay=False):
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        super().__init__(filename, mode, max_bytes, backup_count, encoding, delay)


base_rotating_handler = {
    'class': 'django-logger.logger_handlers.RotationFileHandler',
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
        'max_bytes': 2 ** 20,
        'backup_count': 0,
        'filename': f'logs/Information/INFO.log',
        'filters': ['info_filter'],
    },
    'rotating_file_handler_error': {
        **base_rotating_handler,
        'max_bytes': 2 ** 20,
        'backup_count': 10,
        'filename': f'logs/Errors/ERROR.log',
        'filters': ['error_filter'],
    },
    'rotating_file_handler_critical': {
        **base_rotating_handler,
        'max_bytes': 10 * (2 ** 20),
        'backup_count': 100,
        'filename': f'logs/Critical/CRITICAL.log',
        'filters': ['critical_filter'],
    },
}
