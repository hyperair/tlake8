#!/usr/bin/env python

from distutils.core import setup

setup(
    name='tlake8',
    version='0.1',
    description='flake8 for tab junkies',
    author='Chow Loong Jin',
    author_email='hyperair@debian.org',
    url='https://www.github.com/hyperair/tlake8',
    scripts=['bin/tlake8'],
    packages=['tlake8'],
    install_requires=['flake8']
)
