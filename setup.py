#!/usr/bin/env python

from setuptools import setup

setup(name='target-stitch',
      version='0.11.0.alpha.2',
      description='Singer.io target for the Stitch API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['target_stitch'],
      install_requires=[
          'jsonschema==2.6.0',
          'mock==2.0.0',
          'singer-python==2.1.4',
          'stitchclient==0.6.0',
          'strict-rfc3339',
          'python-dateutil==2.6.1',
      ],
      entry_points='''
          [console_scripts]
          target-stitch=target_stitch:main
      ''',
      packages=['target_stitch'],
)
