from freezegun import freeze_time

from {{cookiecutter.py_namespace}} import {{cookiecutter.py_namespace}}


@freeze_time('2016-01-01 00:00:00')
def test_pretty_format_date():
    assert {{cookiecutter.py_namespace}}.format_datetime() == '2016-01-01 00:00:00'
