#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import join, dirname

import gitcheck

setup(name='gitcheck',
      version = gitcheck.__version__,
      author = gitcheck.__author__ , 
      author_email = gitcheck.__email__,
      url = 'http://github.com/johnjosephhorton/gitcheck',
      packages = [''],
      package_data = {'':['*.md', 'checklists/*.md']},
      package_dir= {'':'.'}, 
      entry_points={
          'console_scripts':
              ['gitcheck = gitcheck:main',
               ]}, 
      classifiers=(
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License v3 or '
          'later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      )
      )

