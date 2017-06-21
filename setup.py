#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Setup script for the minixsv library
#
# Usage: python setup.py install
#

from distutils.core import setup
#from setuptools import setup

LONG_DESCRIPTION = '''\
minixsv is a lightweight XML schema validator written in "pure" Python
Currently a subset of the XML schema standard is supported minixsv is
based on genxmlif, a generic XML interface class, which currently
supports minidom, elementtree or 4DOM/pyXML as XML parser Other parsers
can be adapted by implementing an appropriate derived interface class
'''

setup(name='minixsv',
      version='0.9.1',
      description='A lightweight XML schema validator written in pure Python',
      long_description = LONG_DESCRIPTION,
      author='Roland Leuthe',
      author_email='roland@leuthe-net.de',
      url='http://www.leuthe-net.de/MiniXsv.html',
      license='Python (MIT style)',
      platforms='Python 2.4 and later',
      classifiers=["Development Status :: 4 - Beta",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: Python (MIT style)",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.6",
                   "Topic :: Text Processing :: Markup :: XML",
                   "Topic :: Software Development :: Libraries :: Python Modules",
                  ],
      packages=['minixsv', 'genxmlif'],
      package_data={'minixsv': ['datatypes.xsd',
                                'xml.xsd',
                                'XMLSchema.xsd',
                                'XMLSchema-instance.xsd',
                                'XInclude.xsd',
                                'README.txt',
                                'minixsv'],
                     'genxmlif':['README.txt']},
     )
