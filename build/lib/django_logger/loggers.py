loggers = {
    'django-logger': {
        'handlers': ['console', 'rotating_file_handler_info', 'rotating_file_handler_error',
                     'rotating_file_handler_critical'],
        'level': 'INFO',
        'propagate': False,
    },
}
