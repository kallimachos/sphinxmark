#!/bin/python3
# coding: utf-8
"""sphinxmark setup file."""

# To use a consistent encoding
from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sphinxmark',
    version='0.1.0',
    description='A Sphinx extension that enables watermarks for HTML output.',
    long_description=long_description,
    url='https://github.com/kallimachos/sphinxmark',
    author='Brian Moss',
    author_email='kallimachos@gmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Documentation :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='sphinx documentation watermark',

    packages=find_packages(exclude=['doc', 'tools', 'tests']),

    install_requires=['bottle'],

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'sphinxmark': ['watermark-draft.png', 'watermark.tpl'],
    },
)
