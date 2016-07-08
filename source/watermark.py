#!/bin/python3
# coding: utf-8
"""A Sphinx extension that enables watermarks for HTML output."""

import logging
import os
import shutil

from bottle import TEMPLATE_PATH, template

# append source directory to bottle.TEMPLATE_PATH so template is found
SRCDIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_PATH.append(SRCDIR)

logging.basicConfig(level=logging.DEBUG)


def watermark(app, env):
    """Add watermark."""
    if app.config.watermark_enable is True:
        if not os.path.exists(app.config.html_static_path[0]):
            os.makedirs('_static')
            staticpath = '_static'
        else:
            staticpath = app.config.html_static_path[0]

        default_image = os.path.join(SRCDIR, 'watermark-draft.png')
        shutil.copy(default_image, staticpath)

        image = app.config.watermark_image
        logging.debug("Image: " + image)

        css = template('watermark', image=image)
        logging.debug("Template: " + css)

        cssfile = os.path.join(staticpath, 'watermark.css')
        logging.debug("cssfile: " + cssfile)

        with open(cssfile, 'w') as f:
            f.write(css)
        app.add_stylesheet(cssfile)


def setup(app):
    """Setup for Sphinx ext."""
    app.add_config_value('watermark_enable', False, 'html')
    app.add_config_value('watermark_image', 'watermark-draft.png', 'html')
    app.connect('env-updated', watermark)
    return {'version': '0.1'}


if __name__ == '__main__':
    pass
