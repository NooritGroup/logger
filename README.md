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

```shell
pip install git+https://github.com/NooritGroup/logger.git
```

---

## Settings

### Middleware

Add `LoggerMiddleware` to your `MIDDLEWARES` settings:

```python
MIDDLEWARES = [
    ...,
    'django_logger.middleware.LoggerMiddleware'
]
```

### Logger Setting

Add `DJANGO_LOGGER_DATA` to your settings:

```python
DJANGO_LOGGER_DATA = {
    'LOG_PATH': 'logs',  # No default
    'BACKUP_COUNTS': {
        'BACKUP_COUNT_INFO': ...,  # Default is 1
        'BACKUP_COUNT_ERROR': ...,  # Default is 10
        'BACKUP_COUNT_CRITICAL': ...  # Default is 100
    },
    'MAX_BYTES': {
        'MAX_BYTES_INFO': ...,  # Default is 1MB
        'MAX_BYTES_ERROR': ...,  # Default is 1MB
        'MAX_BYTES_CRITICAL': ...,  # Default is 10MB
    },
    'ENCODING': ...  # Default is UTF-8
}
```

## Output

Logs save in the log folder as json by down structure:

```
project_folder/
├─ app/
│ ├─ __init__.py
│ ├─ admin.py
│ ├─ apps.py
│ ├─ views.py
│ ├─ forms.py
│ ├─ models.py
│ └─ urls.py
├─ settings_folder/
│ ├─ __init__.py
│ ├─ asgi.py
│ ├─ settings.py
│ ├─ urls.py
│ └─ wsgi.py
├─ log_folder/
│ ├─ Information/
│ │ └─ INFO.log
│ ├─ Errors/
│ │ └─ ERROR.log
│ └─ Critical/
│   └─ CRITICAL.log
```

And print in the `Console` by down format:

```python
logged:
	{Message} - {Status Code} - {Url} - {Path} - {Method}
	user: {User}
	IP: {IP}
	Session Id: {Session Id}
	Protocol: {Protocol}
	request data: {Request Data}
	response data: {Response Data}
	Sec Ch Ua Platform: {Sec Ch Ua Platform}
	User Agent: {User Agent}
	Accept Encoding: {Accept Encoding}
	Csrf Token: {Csrf Token}
	error: {Error}  # if any
	{Time} - {Level} - {Module}
```

[logger]: https://github.com/NooritGroup/logger