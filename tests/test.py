#!/bin/python3
# coding: utf-8
"""Sphinxmark test file."""

from os import path
from pathlib import Path

import pytest
from sphinx_testing import TestApp as MakeApp  # rename to prevent warning

# defaults = {'sphinxmark_enable': True,
#             'sphinxmark_div': 'default',
#             'sphinxmark_border': None,
#             'sphinxmark_repeat': True,
#             'sphinxmark_fixed': False,
#             'sphinxmark_image': 'default',
#             'sphinxmark_text': 'default',
#             'sphinxmark_text_color': (255, 0, 0),
#             'sphinxmark_text_size': 100,
#             'sphinxmark_text_width': 1000,
#             'sphinxmark_text_opacity': 20,
#             'sphinxmark_text_spacing': 400,
#             'sphinxmark_text_rotation': 0}

htmlfile = 'index.html'
cssfile = '_static/sphinxmark.css'
htmlresult = ('<link rel="stylesheet" type="text/css" href="%s" />' % cssfile)


def test_defaults():
    """Test defaults."""
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True)
    app.builder.build_all()
    assert app.config.sphinxmark_div == 'default'
    assert app.config.sphinxmark_repeat is True
    assert app.config.sphinxmark_border is None
    assert app.config.sphinxmark_fixed is False
    assert app.config.sphinxmark_image == 'default'
    assert app.config.sphinxmark_text == 'default'
    assert app.config.sphinxmark_text_color == (255, 0, 0)
    assert app.config.sphinxmark_text_size == 100
    assert app.config.sphinxmark_text_width == 1000
    assert app.config.sphinxmark_text_opacity == 20
    assert app.config.sphinxmark_text_spacing == 400
    assert app.config.sphinxmark_text_rotation == 0

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ('url("watermark-draft.png")') in css


def test_div():
    """Test div."""
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_div': 'body-test'})
    app.builder.build_all()
    assert app.config.sphinxmark_div == 'body-test'

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ('div.body-test') in css


def test_border():
    """Test border."""
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_border': 'left'})
    app.builder.build_all()
    assert app.config.sphinxmark_border == 'left'

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ('border-left') in css


def test_repeat():
    """Text repeat."""
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True)
    app.builder.build_all()
    assert app.config.sphinxmark_repeat is True

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ('background-repeat: repeat-y !important;') in css


def test_no_repeat():
    """Text no repeat."""
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_repeat': False})
    app.builder.build_all()
    assert app.config.sphinxmark_repeat is False

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ('background-repeat: no-repeat !important;') in css


def test_fixed():
    """Test fixed."""
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_fixed': True})
    app.builder.build_all()
    assert app.config.sphinxmark_fixed is True

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ('background-attachment: fixed') in css


def test_image():
    """Test image."""
    image = 'new.png'
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': image})
    app.builder.build_all()
    assert app.config.sphinxmark_image == image

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    cssresult = 'url("%s")' % image
    assert cssresult in css


def test_imagefail():
    """Test image not found raises TypeError."""
    image = 'fail.png'
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': image})
    with pytest.raises(TypeError):
        app.builder.build_all()
    assert app.config.sphinxmark_image == image

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    cssresult = 'url("%s")' % image
    assert cssresult not in css


def test_textmark():
    """Test textmark."""
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': 'text',
                                 'sphinxmark_text': 'Mitaka'})
    app.builder.build_all()
    assert app.config.sphinxmark_image == 'text'
    assert app.config.sphinxmark_text == 'Mitaka'

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ('url("textmark_Mitaka.png")') in css


def test_static():
    """Test static."""
    image = 'sample.png'
    htmlpath = ['static']
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': image,
                                 'html_static_path': htmlpath})
    app.builder.build_all()
    assert app.config.sphinxmark_image == image
    assert app.config.html_static_path == htmlpath

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    cssresult = 'url("%s")' % image
    assert cssresult in css


def test_staticfail():
    """Test static not found raises TypeError."""
    image = 'new.png'
    htmlpath = ['static']
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': image,
                                 'html_static_path': htmlpath})
    with pytest.raises(TypeError):
        app.builder.build_all()
    assert app.config.sphinxmark_image == image
    assert app.config.html_static_path == htmlpath

    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html

    css = Path(path.join(app.outdir, cssfile)).read_text()
    cssresult = 'url("%s")' % image
    assert cssresult not in css


if __name__ == '__main__':
    pass
