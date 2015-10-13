#!/usr/bin/env python3
import os
import sys
import doctest
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# TODO change verison
VERSION = '0.0.1'

name = 'webassets_ng_annotate'
with open('README.md') as readme_file:
    readme = readme_file.read()

if sys.argv[-1] == 'publish':
    if not doctest.testfile('README.md', verbose=True).failed:
        os.system('python setup.py sdist upload')
        sys.exit(0)

setup(**{
    'name': name,
    'url': 'https://github.com/imbolc/%s' % name.replace('_', '-'),
    'version': VERSION,
    'description': readme.split('===\n')[1].strip().split('\n\n')[0],
    'long_description': readme,

    'py_modules': [name],
    'install_requires': ['webassets'],

    'author': 'Imbolc',
    'author_email': 'imbolc@imbolc.name',
    'license': 'ISC',

    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
})
