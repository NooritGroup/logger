<h1 align="center">
        [![django-logger]][logger]
</h1>

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

Add `LoggerMiddleware` to your `MIDDLEWARES` settings:

```python
MIDDLEWARES = [
    ...,
    "django-logger.middleware.LoggerMiddleware"
]
```

[logger]: https://github.com/NooritGroup/logger
