==========
sphinxmark
==========

**sphinxmark** is an extension for Sphinx that enables watermarks for
HTML output.

Source code: https://github.com/kallimachos/sphinxmark


Installation
~~~~~~~~~~~~

Install sphinxmark using pip:

.. code::

   $ pip install sphinxmark


Usage
~~~~~

Configure sphinxmark in your ``conf.py`` file.

#. Add sphinxmark to the list of extensions:

   .. code::

      extensions = ['sphinxmark']

#. If you are using a custom image file, specify its directory relative
   to the ``conf.py`` file. If no value is given, the path defaults to
   ``_static``.

   .. code::

      html_static_path = ['_static']

#. Enable sphinxmark and set options as required:

   .. code::

      sphinxmark_enable = True
      sphinxmark_div = 'default'
      sphinxmark_image = 'text'
      sphinxmark_text = 'Pre-Release'
      sphinxmark_text_size = 80


Options
~~~~~~~

sphinxmark_enable (bool)
   - ``True`` - enable watermarks
   - ``False`` - disable watermarks
   - Default = False
   - Example:

     ``sphinxmark_enable = True``

sphinxmark_div (string)
   - CSS div where watermark is displayed
   - sphinxmark provides a template css file that uses the specified image
     as the watermark for any area defined as ``div.body`` by default. This
     setting works for the default Sphinx theme. To use
     sphinxmark with themes that have the document body in a different div,
     specify the div using the ``sphinxmark_div`` option.
   - Default = 'body'
   - Examples:

     sphinx_rtd_theme -> ``sphinxmark_div = 'document'``

     openstackdocstheme -> ``sphinxmark_div = 'docs-body'``

sphinxmark_image (string)
   - image file in ``html_static_path`` directory to use as watermark
   - ``text`` selects the text-based watermark specified in the
     ``sphinxmark_text`` option
   - if no image is specified, a default DRAFT watermark image is used
   - Default = 'default'
   - Examples:

     ``sphinxmark_image = 'preview_mark.png'``

     ``sphinxmark_image = 'text'``

sphinxmark_text (string)
   - Text to use for watermark when ``text`` option is selected in
     ``sphinxmark_image``
   - Default = 'default'
   - Example:

     ``sphinxmark_text = 'Preview'``

sphinxmark_text_size (int)
   - Font size for text specified in ``sphinxmark_text``
   - Default = 100
   - Example:

     ``sphinxmark_text_size = 100``

sphinxmark_text_color (tuple)
   - RGB color code for text specified in ``sphinxmark_text``.
   - Default = (255, 0, 0)
   - Example:

     ``sphinxmark_text_color = (255, 0, 0)``

sphinxmark_text_opacity (int)
   - Opacity (RGB Alpha) for text specified in ``sphinxmark_text``
   - Default = 40
   - Example:

     ``sphinxmark_text_opacity = 40``

sphinxmark_debug (bool)
   - ``True`` - enable debug level logging
   - ``False`` - disable debug level logging
   - Default = False
   - Example:

     ``sphinxmark_debug = True``


Source code
~~~~~~~~~~~

.. automodule:: __init__
   :members:
