#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='shutilwhich',
    version='1.1.0',
    description='shutil.which for those not using Python 3.3 yet.',
    long_description=read('README.rst'),
    author='Marc Brinkmann',
    author_email='git@marcbrinkmann.de',
    url='http://github.com/mbr/shutilwhich',
    license='PSF',
    packages=find_packages(exclude=['tests']),
)
