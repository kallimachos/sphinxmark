#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables watermarks for HTML output.

https://github.com/kallimachos/sphinxmark

Copyright 2021 Brian Moss

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from pathlib import Path
from shutil import copy

from bottle import TEMPLATE_PATH, template
from PIL import Image, ImageDraw, ImageFont
from sphinx.application import Sphinx
from sphinx.environment import BuildEnvironment
from sphinx.util import logging

LOG = logging.getLogger(__name__)


def buildcss(app: Sphinx, buildpath: str, imagefile: str) -> str:
    """Create CSS file."""
    # set default values
    div = "body"
    repeat = "repeat-y"
    position = "center"
    attachment = "scroll"

    if app.config.sphinxmark_div != "default":
        div = app.config.sphinxmark_div

    if app.config.sphinxmark_repeat is False:
        repeat = "no-repeat"

    if app.config.sphinxmark_fixed is True:
        attachment = "fixed"

    border = app.config.sphinxmark_border
    if border == "left" or border == "right":
        css = template("border", div=div, image=imagefile, side=border)
    else:
        css = template(
            "watermark",
            div=div,
            image=imagefile,
            repeat=repeat,
            position=position,
            attachment=attachment,
        )
    LOG.debug(f"[sphinxmark] Template: {css}")
    cssname = "sphinxmark.css"
    cssfile = Path(buildpath, cssname)

    with open(cssfile, "w") as f:
        f.write(css)

    return cssname


def createimage(app: Sphinx, srcdir: Path, buildpath: Path) -> str:
    """Create PNG image from string."""
    text = app.config.sphinxmark_text

    # draw transparent background
    width = app.config.sphinxmark_text_width
    height = app.config.sphinxmark_text_spacing
    img = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    d = ImageDraw.Draw(img)

    # set font
    fontfile = str(Path(srcdir, "arial.ttf"))
    font = ImageFont.truetype(fontfile, app.config.sphinxmark_text_size)

    # set x y location for text
    xsize, ysize = d.textsize(text, font)
    LOG.debug("[sphinxmark] x = " + str(xsize) + "\ny = " + str(ysize))
    x = (width / 2) - (xsize / 2)
    y = (height / 2) - (ysize / 2)

    # add text to image
    color = app.config.sphinxmark_text_color
    d.text((x, y), text, font=font, fill=color)

    # set opacity
    img2 = img.copy()
    img2.putalpha(app.config.sphinxmark_text_opacity)
    img.paste(img2, img)

    # rotate image
    img = img.rotate(app.config.sphinxmark_text_rotation)

    # save image
    imagefile = f"textmark_{text}.png"
    imagepath = Path(buildpath, imagefile)
    img.save(imagepath, "PNG")
    LOG.debug(f"[sphinxmark] Image saved to: {imagepath}")

    return imagefile


def getimage(app: Sphinx) -> tuple:
    """Get image file."""
    # append source directory to TEMPLATE_PATH so template is found
    srcdir = Path(__file__).parent.resolve()
    TEMPLATE_PATH.append(srcdir)
    staticbase = "_static"
    buildpath = Path(app.outdir, staticbase)
    try:
        buildpath.mkdir()
    except OSError:
        if not buildpath.is_dir():
            raise

    if app.config.sphinxmark_image == "default":
        imagefile = "watermark-draft.png"
        imagepath = Path(srcdir, imagefile)
        copy(imagepath, buildpath)
        LOG.debug(f"[sphinxmark] Using default image: {imagefile}")
    elif app.config.sphinxmark_image == "text":
        imagefile = createimage(app, srcdir, buildpath)
        LOG.debug(f"[sphinxmark] Image: {imagefile}")
    else:
        imagefile = app.config.sphinxmark_image

        if app.config.html_static_path:
            staticpath = app.config.html_static_path[0]
        else:
            staticpath = "_static"

        LOG.debug(f"[sphinxmark] static path: {staticpath}")
        confdir = str(app.confdir)
        imagepath = Path(confdir, staticpath, imagefile)
        LOG.debug(f"[sphinxmark] Imagepath: {imagepath}")

        try:
            copy(imagepath, buildpath)
        except FileNotFoundError:
            LOG.info(" fail")
            raise

    return (buildpath, imagefile)


def watermark(app: Sphinx, env: BuildEnvironment) -> None:
    """Add watermark."""
    if app.config.sphinxmark_enable is True:
        LOG.info("adding watermark...", nonl=True)
        try:
            buildpath, imagefile = getimage(app)
            cssname = buildcss(app, buildpath, imagefile)
            app.add_css_file(cssname)
            LOG.info(" done")
        except Exception as e:
            LOG.warning(f"Failed to add watermark: {e}")
    return


def setup(app: Sphinx) -> dict:
    """Configure setup for Sphinx extension.

    :param app: Sphinx application context.
    """
    app.add_config_value("sphinxmark_enable", False, "html")
    app.add_config_value("sphinxmark_div", "default", "html")
    app.add_config_value("sphinxmark_border", None, "html")
    app.add_config_value("sphinxmark_repeat", True, "html")
    app.add_config_value("sphinxmark_fixed", False, "html")
    app.add_config_value("sphinxmark_image", "default", "html")
    app.add_config_value("sphinxmark_text", "default", "html")
    app.add_config_value("sphinxmark_text_color", (255, 0, 0), "html")
    app.add_config_value("sphinxmark_text_size", 100, "html")
    app.add_config_value("sphinxmark_text_width", 1000, "html")
    app.add_config_value("sphinxmark_text_opacity", 20, "html")
    app.add_config_value("sphinxmark_text_spacing", 400, "html")
    app.add_config_value("sphinxmark_text_rotation", 0, "html")
    app.connect("env-updated", watermark)

    return {
        "version": "0.2.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
