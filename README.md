<h1 align="center">django-logger</h1>

# Overview

The django-logger library is for server logging.

---

# Installation

Install using `pip`:

```cmd
pip install git+https://github.com/NooritGroup/logger.git
```

---

# Settings

Add `LoggerMiddleware` to your `MIDDLEWARES` settings:

    MIDDLEWARES = [
    ...
    "django-logger.middleware.LoggerMiddleware"
    ]