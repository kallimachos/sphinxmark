==========
sphinxmark
==========

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

      extensions = [
         'sphinx.ext.autodoc',
         'sphinx.ext.doctest',
         'sphinxmark',
      ]

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
      watermark_debug = False

#. Put images in your static directory and use the ``watermark_image`` option
   to specify a custom watermark image.

.. important::

   The extension provides a template css file that uses the specified image
   as the watermark for any area defined as ``div.body``. Sphinxmark does not
   work with themes that do not place body content in ``div.body``. For this
   reason, sphinxmark does not work with ``sphinx_rtd_theme``.


Future enhancements
~~~~~~~~~~~~~~~~~~~
.. code::

   .. watermark:: Mitaka  # this would work on that page only

Sphinxmark should accept image file or text.


To-do
~~~~~
- add tests
- improve warnings, errors, and exception capture
- make extension work with all themes (or at least all included Sphinx themes
  and ``sphinx_rtd_theme``)


Source code
~~~~~~~~~~~

.. automodule:: __init__
   :members:
