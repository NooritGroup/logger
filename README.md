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

```html
project_folder/
&#x251C;&#x2500; app/
&#x2502;&nbsp;&#x251C;&#x2500; __init__.py
&#x2502;&nbsp;&#x251C;&#x2500; admin.py
&#x2502;&nbsp;&#x251C;&#x2500; apps.py
&#x2502;&nbsp;&#x251C;&#x2500; views.py
&#x2502;&nbsp;&#x251C;&#x2500; forms.py
&#x2502;&nbsp;&#x251C;&#x2500; models.py
&#x2502;&nbsp;&#x2514;&#x2500; urls.py
&#x251C;&#x2500; settings_folder/
&#x2502;&nbsp;&#x251C;&#x2500; __init__.py
&#x2502;&nbsp;&#x251C;&#x2500; asgi.py
&#x2502;&nbsp;&#x251C;&#x2500; settings.py
&#x2502;&nbsp;&#x251C;&#x2500; urls.py
&#x2502;&nbsp;&#x2514;&#x2500; wsgi.py
<strong>
&#x251C;&#x2500; log_folder/
&#x2502;&nbsp;&#x251C;&#x2500; Information/
&#x2502;&nbsp;&#x2502;&nbsp;&#x2514;&#x2500; INFO.log
&#x2502;&nbsp;&#x251C;&#x2500; Errors/
&#x2502;&nbsp;&#x2502;&nbsp;&#x2514;&#x2500; ERROR.log
&#x2502;&nbsp;&#x2514;&#x2500; Critical/
&#x2502;&nbsp;&nbsp;&nbsp;&#x2514;&#x2500; CRITICAL.log
</strong>
```

And print in the `Console` by down format:

```pycon
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