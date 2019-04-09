#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Documentation for testing sphinxmark."""

extensions = ['sphinxmark']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'testmark'
copyright = '2019, Brian'
author = 'Brian'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------
html_theme = 'alabaster'
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'openstackdocs'
# html_theme_path = [openstackdocstheme.get_html_theme_path()]
htmlhelp_basename = 'testmarkdoc'

# -- Options for sphinxmark -----------------------------------------------
sphinxmark_enable = True
# sphinxmark_div = 'docs-body'
# sphinxmark_border = 'left'
# sphinxmark_repeat = False
# sphinxmark_fixed = True
# sphinxmark_image = 'text'
# sphinxmark_text = 'Mitaka'
# sphinxmark_text_color = (255, 0, 0)
# sphinxmark_text_size = 100
# sphinxmark_text_width = 1000
# sphinxmark_text_opacity = 50
# sphinxmark_text_spacing = 600
# sphinxmark_text_rotation = 90
