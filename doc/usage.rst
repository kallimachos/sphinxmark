=====
Usage
=====

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

#. If you define ``html_context`` in your ``conf.py``, you must add the
   ``sphinxmark.css`` style sheet to it.

   .. code::

      html_context = {
        'css_files': [
          '_static/bespoke.css',  # custom CSS styling
          '_static/sphinxmark.css',  # watermark styling
          ],
        }
