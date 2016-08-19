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


Installation
~~~~~~~~~~~~

Install sphinxmark using pip:

   .. code::

      $ pip install sphinxmark


Usage
~~~~~

#. Add sphinxmark to the list of extensions in ``conf.py``:

   .. code::

      extensions = ['sphinxmark']

#. Specify a static directory in ``conf.py`` for your image files. If the
   path does not exist, the sphinxmark extension creates the directory and
   populates it with ``watermark.css`` and ``watermark-draft.png``:

   .. code::

      html_static_path = ['_static']

   .. warning::

      ``watermark.css`` is recreated on each Sphinx run. Edits to this file
      are not retained.

#. Configure sphinxmark in ``conf.py`` as required:

   .. code::

      watermark_enable = True
      watermark_image = 'default'
      watermark_text = 'default'
      watermark_div = 'default'
      watermark_debug = False


Options
~~~~~~~

watermark_enable (bool)
   - ``True`` enable watermarks
   - ``False`` disable watermarks
   - Default = False
   - Example:

     ``watermark_enable = True``

watermark_image (string)
   - image file in ``_static`` directory to use as watermark
   - ``text`` selects the text-based watermark specified in
     ``watermark_text`` option
   - Default = watermark-draft.png (included DRAFT image)
   - Examples:

     ``watermark_image = 'preview_mark.png'``

     ``watermark_image = 'text'``

watermark_text (string)
   - Text to use for watermark when ``text`` option is selected in
     ``watermark_image``
   - Default = default
   - Example:

     ``watermark_text = 'Preview'``

watermark_div (string)
   - CSS div where watermark is displayed
   - sphinxmark provides a template css file that uses the specified image
     as the watermark for any area defined as ``div.body`` by default. To use
     sphinxmark with themes that have the document body in a different div,
     specify the div using the ``watermark_div`` option.
   - Default = body (this works for default Sphinx theme)
   - Examples:

     sphinx_rtd_theme -> ``watermark_div = 'document'``

     openstackdocstheme -> ``watermark_div = 'docs-body'``

watermark_debug (bool)
   - ``True`` enable debugging output during Sphinx build
   - ``False`` disable debugging output during Sphinx build
   - Default = False
   - Example:

     ``watermark_debug = True``
