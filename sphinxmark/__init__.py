#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables watermarks for HTML output.

https://github.com/kallimachos/sphinxmark
"""

import logging

from os import path
from bottle import TEMPLATE_PATH, template
from PIL import Image, ImageDraw, ImageFont


def setstatic(app):
    """Set the static path."""
    staticpath = app.config.html_static_path
    logging.debug('html_static_path: ' + str(staticpath))

    if not staticpath:
        logging.debug('html_static_path not set. Using _static/')
        app.config.html_static_path.append('_static')

    staticpath = path.join(app.confdir, app.config.html_static_path[0])
    logging.debug('static path: ' + staticpath)

    return(staticpath)


def createimage(app, srcdir):
    """Create PNG image from string."""
    text = app.config.sphinxmark_text

    # draw transparent background
    width = 400
    height = 300
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)

    # set font
    fontfile = path.join(srcdir, 'arial.ttf')
    font = ImageFont.truetype(fontfile, app.config.sphinxmark_text_size)

    # set x y location for text
    xsize, ysize = d.textsize(text, font)
    logging.debug('x = ' + str(xsize) + '\ny = ' + str(ysize))
    x = (width / 2) - (xsize / 2)
    y = 20

    # add text to image
    color = app.config.sphinxmark_text_color
    d.text((x, y), text, font=font, fill=color, align="center")

    # set opacity
    img.putalpha(app.config.sphinxmark_text_opacity)

    # save image
    imagename = 'textmark_' + text + '.png'
    imagefile = path.join(srcdir, imagename)
    logging.debug('imagefile: ' + imagefile)
    img.save(imagefile, 'PNG')
    logging.debug('Image saved to: ' + imagefile)

    return(imagename)


def watermark(app, env):
    """Add watermark."""
    if app.config.sphinxmark_debug is True:
        logging.basicConfig(level=logging.DEBUG)

    app.info('adding watermark...', nonl=True)

    if app.config.sphinxmark_enable is True:
        # append source directory to TEMPLATE_PATH so template is found
        srcdir = path.abspath(path.dirname(__file__))
        TEMPLATE_PATH.append(srcdir)

        if app.config.sphinxmark_image == 'default':
            imagefile = path.join(srcdir, 'watermark-draft.png')
            logging.debug('Using default image: ' + imagefile)

        elif app.config.sphinxmark_image == 'text':
            imagefile = createimage(app, srcdir)
            logging.debug('Image: ' + imagefile)

        else:
            staticpath = setstatic(app)
            image = app.config.sphinxmark_image
            logging.debug('Image: ' + image)
            imagefile = path.abspath(path.join(staticpath, image))
            logging.debug('Imagefile: ' + imagefile)
            if path.exists(imagefile) is False:
                logging.error("Cannot find '%s'. Put watermark images in '%s'",
                              image, staticpath)

        if app.config.sphinxmark_div == 'default':
            div = 'body'
        else:
            div = app.config.sphinxmark_div

        css = template('watermark', div=div, image=imagefile)
        logging.debug("Template: " + css)

        cssfile = path.abspath(path.join(srcdir, 'temp.css'))
        with open(cssfile, 'w') as f:
            f.write(css)
        app.add_stylesheet(cssfile)
        app.info(' done')


def setup(app):
    """Setup for Sphinx ext."""
    logging.basicConfig(format='%(levelname)s:sphinxmark: %(message)s')
    try:
        app.add_config_value('sphinxmark_enable', False, 'html')
        app.add_config_value('sphinxmark_div', 'default', 'html')
        app.add_config_value('sphinxmark_image', 'default', 'html')
        app.add_config_value('sphinxmark_text', 'default', 'html')
        app.add_config_value('sphinxmark_text_color', (255, 0, 0), 'html')
        app.add_config_value('sphinxmark_text_size', 100, 'html')
        app.add_config_value('sphinxmark_text_opacity', 40, 'html')
        app.add_config_value('sphinxmark_debug', False, 'html')
        app.connect('env-updated', watermark)
    except:
        logging.error('Failed to add watermark.')
    return {'version': '0.1'}


if __name__ == '__main__':
    pass
