from logging import Filter


class LevelFilter(Filter):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelname == self.level


filters = {
    'info_filter': {
        '()': 'django-logger.logger_filters.LevelFilter',
        'level': 'INFO',
    },
    'error_filter': {
        '()': 'django-logger.logger_filters.LevelFilter',
        'level': 'ERROR',
    },
    'critical_filter': {
        '()': 'django-logger.logger_filters.LevelFilter',
        'level': 'CRITICAL',
    },
}
