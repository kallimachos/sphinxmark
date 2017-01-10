=======
Options
=======

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

sphinxmark_border (string)
   - ``left`` - place watermark on left border
   - ``right`` - place watermark on right border
   - setting the ``sphinxmark_border`` option overrides the
     ``sphinxmark_repeat`` and ``sphinxmark_fixed`` options.
   - when using a text watermark, adjust the ``sphinxmark_text`` options
     to achieve the desired appearance.
   - Default = None
   - Example:

     ``sphinxmark_border = 'left'``

sphinxmark_repeat (bool)
   - ``True`` - image repeats down the page
   - ``False`` - image appears once at top of page
   - Default = True
   - Example:

     ``sphinxmark_repeat = True``

sphinxmark_fixed (bool)
   - ``True`` - watermark does not scroll with content
   - ``False`` - watermark scrolls with content
   - When set to ``True``, this option centers the watermark in the viewport,
     not the div specified by ``sphinxmark_div``.
   - Default = False
   - Example:

     ``sphinxmark_fixed = False``

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

sphinxmark_text_width (int)
   - Width of transparent box containing text specified in ``sphinxmark_text``
   - If a large ``sphinxmark_text_size`` is specified, or the
     ``sphinxmark_text`` string is long, you may need to set this option
     to a number higher than the default for the entire string to display. Note
     that the text will be cut off at the edge of the containing CSS div
     regardless of the ``sphinxmark_text_width`` setting.
   - Default = 1000
   - Example:

      ``sphinxmark_text_width = 1000``

sphinxmark_text_color (tuple)
   - RGB color code for text specified in ``sphinxmark_text``.
   - Default = (255, 0, 0)
   - Example:

     ``sphinxmark_text_color = (255, 0, 0)``

sphinxmark_text_opacity (int)
   - Opacity (RGB Alpha) for text specified in ``sphinxmark_text``
   - Default = 20
   - Example:

     ``sphinxmark_text_opacity = 20``

sphinxmark_text_spacing (int)
   - Set spacing between text watermarks
   - Default = 400
   - Example:

      ``sphinxmark_text_spacing = 400``

sphinxmark_text_rotation (int)
   - Text watermark rotation
   - Default = 0
   - Example:

     ``sphinxmark_text_rotation = 90``
