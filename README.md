<h1 align="center">
    <a style="font-size: 10vw; color: rgb(0, 255, 255)" href="https://github.com/NooritGroup/logger">
        django-logger
    </a>
</h1>

## Overview

The **django-logger** library is for server logging.

**django-logger** has log three level :

* <strong style="color: blue">INFO</strong>
* <strong style="color: orange">ERROR</strong>
* <strong style="color: red">CRITICAL</strong>

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