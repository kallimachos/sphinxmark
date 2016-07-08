================
sphinx-watermark
================

.. image:: https://travis-ci.org/kallimachos/sphinx-watermark.svg?branch=master
   :target: https://travis-ci.org/kallimachos/sphinx-watermark

.. image:: https://img.shields.io/badge/Python-3.4-brightgreen.svg?style=flat
   :target: http://python.org

.. image:: http://img.shields.io/badge/license-GPL-blue.svg?style=flat
   :target: http://opensource.org/licenses/GPL-3.0

sphinx-watermark is an extension for Sphinx that enables watermarks for
HTML output.


Spec
~~~~

.. code::

   .. watermark:: Mitaka  # this would work on that page only

This can be added the propend section of conf.py so it affects the whole
document

Should accept image file or text


Useful modules
~~~~~~~~~~~~~~

Sphinx.add_stylesheet(filename)[source]

   Add filename to the list of CSS files that the default HTML template will
   include. Like for add_javascript(), the filename must be relative to the
   HTML static path, or a full URI with scheme.

Perhaps I can just use the ``.. raw::`` directive to pass some CSS through.