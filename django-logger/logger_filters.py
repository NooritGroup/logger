from logging import Filter


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
    'error_filter': {
        '()': LevelFilter,
        'level': 'ERROR',
    },
    'critical_filter': {
        '()': LevelFilter,
        'level': 'CRITICAL',
    },
}
