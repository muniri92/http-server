# -*- coding: utf-8 -*-
"""Setup for http server."""

from setuptools import setup, find_packages



setup(
    name="http-server",
    description="A simple http server",
    version=0.1,
    author="David Flegal, Munir Ibrahim",
    author_email="flegal.david@gmail.com",
    license="MIT",
    py_modules=["server2.py"],
    packages=find_packages(),
    install_requires=["io", "os", "socket"],
    extras_require={'test': ['pytest', 'pytest-xdist', "tox"]},
    )