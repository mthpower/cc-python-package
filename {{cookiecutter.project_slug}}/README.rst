=============================
{{cookiecutter.project_name}}
=============================

.. contents::


{{cookiecutter.project_short_description}}


Quickstart
----------

Prerequisites:

* Python == 3.5
* Docker

A Makefile is provided with common tasks::

    $ make help

    clean - remove build artifacts and python artifacts
    .env - make a virtual environment
    lint - check style with flake8
    isort - check import order with isort
    test - run tox
