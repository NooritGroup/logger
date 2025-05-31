# [Django Logger][logger]

## Overview

The **django-logger** library is for server logging.

**django-logger** has log three level :

* **INFO**
* **ERROR**
* **CRITICAL**

---

## Requirements

### Programming Language

* Python 3

### Library

* python
    * Django
    * Django Rest Framework
    * Jdatetime
    * Python Json Logger

---

## Installation

Install using `pip`:

```cmd
pip install git+https://github.com/NooritGroup/logger.git
```

---

## Settings

### Mandatory

Add `LoggerMiddleware` to your `MIDDLEWARES` settings:

```python
MIDDLEWARES = [
    ...,
    'django_logger.middleware.LoggerMiddleware'
]
```

Add `LOG_DATA` to your settings:

```python
LOG_DATA = {
    'LOG_PATH': 'logs',  # No default
    'BACKUP_COUNTS': {
        'BACKUP_COUNT_INFO': ...,  # Default is 0
        'BACKUP_COUNT_ERROR': ...,  # Default is 10
        'BACKUP_COUNT_CRITICAL': ...  # Default is 100
    },
    'MAX_BYTES': {
        'MAX_BYTES_INFO': ...,  # Default is 1MB
        'MAX_BYTES_ERROR': ...,  # Default is 1MB
        'MAX_BYTES_CRITICAL': ...,  # Default is 10MB
    },
    'ENCODING': ...  # Default is UTF-32
}
```

### Optional

Add `META_ALLOWED_KEYS` to your settings:

```python
META_ALLOWED_KEYS = ...  # Default is ('REMOTE_ADDR', 'HTTP_USER_AGENT', 'HTTP_HOST', 'HTTP_REFERER', 'SERVER_NAME', 'HTTP_ACCEPT')
```

[logger]: https://github.com/NooritGroup/logger
