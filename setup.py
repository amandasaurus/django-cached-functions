#! /usr/bin/env python

from setuptools import setup, find_packages

setup(name="django-cache-properties",
      version="0.1",
      author="Rory McCann",
      author_email="rory@technomancy.org",
      py_modules=['django_cache_property'],
      license = 'GPLv3',
      description = 'Prevent expensive computations by storing low level calues in the django cache',
)
