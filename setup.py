from setuptools import setup, find_packages

setup(
    name='django-logger',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/NooritGroup/logger',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3',
    install_requires=[
        'django',
        'djangorestframework',
        'jdatetime',
        'python-json-logger',
    ]
)
