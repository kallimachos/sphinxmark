==========
sphinxmark
==========

.. image:: https://travis-ci.org/kallimachos/sphinxmark.svg?branch=master
   :target: https://travis-ci.org/kallimachos/sphinxmark

.. image:: https://img.shields.io/pypi/status/sphinxmark.svg?style=flat
   :target: https://pypi.python.org/pypi/sphinxmark

.. image:: https://img.shields.io/pypi/v/sphinxmark.svg?style=flat
   :target: https://pypi.python.org/pypi/sphinxmark

.. image:: https://img.shields.io/badge/Python-2.7-brightgreen.svg?style=flat
   :target: http://python.org

.. image:: https://img.shields.io/badge/Python-3.4-brightgreen.svg?style=flat
   :target: http://python.org

.. image:: http://img.shields.io/badge/license-GPL-blue.svg?style=flat
   :target: http://opensource.org/licenses/GPL-3.0

**sphinxmark** is an extension for Sphinx that enables watermarks for
HTML output.

Full documentation: https://kallimachos.github.io/sphinxmark/


Usage
~~~~~

#. Install sphinxmark:

   .. code::

      $ pip install sphinxmark

#. Add sphinxmark to the list of extensions in ``conf.py``:

   .. code::

      extensions = ['sphinxmark']

#. Specify a static directory in ``conf.py`` for your image files. If the
   path does not exist, the sphinxmark extension creates the directory and
   populates it with ``watermark.css`` and ``watermark-draft.png``:

   .. code::

      html_static_path = ['_static']

   .. note::

      ``watermark.css`` is recreated on each Sphinx run. Edits to this file
      are not retained.

#. Configure sphinxmark in ``conf.py`` as required:

   .. code::

      watermark_enable = True
      watermark_image = 'default'
      watermark_div = 'default'
      watermark_debug = False

#. Put images in your static directory and use the ``watermark_image`` option
   to specify a custom watermark image.

.. note::

   The extension provides a template css file that uses the specified image
   as the watermark for any area defined as ``div.body`` by default. To use
   sphinxmark with themes that have the document body in a different div,
   specify the div using the ``watermark_div`` option.

   For example, for the ``sphinx_rtd_theme``,
   use ``watermark_div = 'document'``.

   For ``openstackdocstheme``,
   use ``watermark_div = 'docs-body'``.
