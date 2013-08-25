# -*- coding: utf-8 -*-
"""
    zt.manticore
    ~~~~~~~~~~~~

    This package is a namespace package that contains all code
    distributed in the ``manticore`` distribution.

    :copyright: Copyright 2010-2013 by the Manticore team.
    :license: BSD, see LICENSE for details.
"""

# this is a namespace package
try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    pass
