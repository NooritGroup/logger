from .logger_filters import filters
from .logger_formatter import formatter
from .logger_handlers import handlers
from .loggers import loggers

django_logger = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': filters,
    'formatters': formatter,
    'handlers': handlers,
    'loggers': loggers,
}
