#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables watermarks for HTML output.

Options:
    watermark_enable = True|False (default=False)

    watermark_image = 'default' (image file; default=watermark-draft.png)

    watermark_debug = True|False (default=False)
"""

import logging
import os
import shutil

from bottle import TEMPLATE_PATH, template


def setstatic(app):
    """Set the static path, and create static directory if required."""
    staticpath = app.config.html_static_path
    logging.debug('html_static_path: ' + str(app.config.html_static_path))

    if not staticpath:
        logging.error('Config error: set `html_static_path` in conf.py')
        return 1
    else:
        staticpath = app.config.html_static_path[0]
        logging.debug("Using '" + staticpath + "' as static path.")

    if not os.path.exists(staticpath):
        logging.debug('Watermark: Creating ' + staticpath)
        os.makedirs(staticpath)

    return(staticpath)


def watermark(app, env):
    """Add watermark."""
    if app.config.watermark_debug is True:
        logging.basicConfig(level=logging.DEBUG)

    if app.config.watermark_enable is True:
        staticpath = setstatic(app)

        if staticpath is 1:
            logging.error('Failed to add watermark.')
            return

        # append source directory to TEMPLATE_PATH so template is found
        srcdir = os.path.abspath(os.path.dirname(__file__))
        TEMPLATE_PATH.append(srcdir)

        if app.config.watermark_image == 'default':
            image = os.path.join(srcdir, 'watermark-draft.png')
            logging.debug('Using default image: ' + image)
            shutil.copy(image, staticpath)
            logging.debug("Copying '" + image + "' to '" + staticpath + "'")
        else:
            image = app.config.watermark_image
            logging.debug('Image: ' + image)

        image = os.path.basename(image)
        if os.path.exists(os.path.join(staticpath, image)) is False:
            logging.error("Cannot find '%s'. Place watermark images in '%s'",
                          image, staticpath)
        cssfile = 'watermark.css'
        css = template('watermark', image=image)
        logging.debug("Template: " + css)

        with open(os.path.join(staticpath, cssfile), 'w') as f:
            f.write(css)
        app.info('adding watermark...', nonl=True)
        app.add_stylesheet(cssfile)
        app.info(' done')


def setup(app):
    """Setup for Sphinx ext."""
    logging.basicConfig(format='%(levelname)s:Watermark: %(message)s')
    try:
        app.add_config_value('watermark_enable', False, 'html')
        app.add_config_value('watermark_image', 'default', 'html')
        app.add_config_value('watermark_debug', False, 'html')
        app.connect('env-updated', watermark)
    except:
        logging.error('Failed to add watermark.')
    return {'version': '0.1'}


if __name__ == '__main__':
    pass
