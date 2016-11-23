import os
import re
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

with open('{{cookiecutter.py_namespace}}/__init__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

setup(
    name='{{cookiecutter.project_slug}}',
    version=version,
    packages=('{{cookiecutter.py_namespace}}',),
    description='{{cookiecutter.project_short_description}}',
    long_description=README,
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    zip_safe=True,
    classifiers=[
        "Private :: Don't upload",
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            '{{cookiecutter.project_slug}} = {{cookiecutter.py_namespace}}.{{cookiecutter.py_namespace}}:main',
        ],
    },
)
