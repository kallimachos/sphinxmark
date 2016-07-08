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

Initial
-------
Import extension in conf.py, which then provides config options for
specifying an image file to use as a watermark for the whole document.

The extension provides a template css file that inserts the specified image
as the watermark to any area defined as ``div.body``.

The extension runs the ``Sphinx.add_stylesheet`` function to add the watermark
stylesheet.


Future
------
.. code::

   .. watermark:: Mitaka  # this would work on that page only

This can be added the propend section of conf.py so it affects the whole
document

Should accept image file or text.


Useful modules
~~~~~~~~~~~~~~

Sphinx.add_stylesheet(filename)[source]

   Add filename to the list of CSS files that the default HTML template will
   include. Like for add_javascript(), the filename must be relative to the
   HTML static path, or a full URI with scheme.

Perhaps I can just use the ``.. raw::`` directive to pass some CSS through.


Execution
~~~~~~~~~

- Module needs to be pip installable.
- Read config info from conf.py
  - watermark_enable: True|False
  - watermark_image: <path/to/image>
- Create watermark.css in static path specified in conf.py with image file
  specified in conf.py
-