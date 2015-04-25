#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.1.1.dev1'

import shutil

if not hasattr(shutil, 'which'):
    from .lib import which
    shutil.which = which
else:
    from shutil import which
