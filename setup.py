#!/bin/python3
# coding: utf-8
"""sphinxmark setup file."""

# To use a consistent encoding
from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sphinxmark',
    version='0.1.15',
    description='A Sphinx extension that enables watermarks for HTML output.',
    long_description=long_description,
    url='https://github.com/kallimachos/sphinxmark',
    author='Brian Moss',
    author_email='kallimachos@gmail.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Documentation :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='sphinx documentation watermark',

    packages=['sphinxmark'],

    package_data={
        'sphinxmark': ['watermark-draft.png', 'border.tpl',
                       'watermark.tpl', 'arial.ttf'],
    },

    install_requires=[
        'bottle<=0.12.10',
        'Pillow<=3.4.1',
    ],
)
