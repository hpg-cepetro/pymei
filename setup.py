#!/usr/bin/env python

from distutils.core import setup

setup(name='pymei',
        version='1.0',
        description='Python library for reading SU and SEG-Y files',
        py_modules=['pymei'],
        scripts=[
            'pmgeometry',
            'pmrotate',
            'pmcontinuity',
            'pmrange',
            'pmbin',
            'pmsort',
            'pmfold',
            'pmmax'],
        )
