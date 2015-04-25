#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil

if not hasattr(shutil, 'which'):
    from .lib import which
    shutil.which = which
else:
    from shutil import which
