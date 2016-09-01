#!/bin/python3
# coding: utf-8
"""Sphinxmark test file."""

from pytest import mark
from sphinx_testing import TestApp as MakeApp  # rename to prevent warning

xfail = mark.xfail

# defaults = {'sphinxmark_enable': True,
#             'sphinxmark_div': 'default',
#             'sphinxmark_image': 'default',
#             'sphinxmark_text': 'default',
#             'sphinxmark_text_color': (255, 0, 0),
#             'sphinxmark_text_size': 100,
#             'sphinxmark_text_opacity': 40}

htmlfile = 'index.html'
htmlresult = ('<link rel="stylesheet" ' +
              'href="_static/sphinxmark.css" type="text/css" />')
cssfile = '_static/sphinxmark.css'


def test_defaults():
    """Test defaults."""
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True)
    app.builder.build_all()
    assert app.config.sphinxmark_div == 'default'
    assert app.config.sphinxmark_image == 'default'
    assert app.config.sphinxmark_text == 'default'
    assert app.config.sphinxmark_text_color == (255, 0, 0)
    assert app.config.sphinxmark_text_size == 100
    assert app.config.sphinxmark_text_opacity == 40

    html = (app.outdir / htmlfile).read_text()
    assert htmlresult in html

    css = (app.outdir / cssfile).read_text()
    assert ('url("watermark-draft.png")') in css


def test_textmark():
    """Test textmark."""
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': 'text',
                                 'sphinxmark_text': 'Mitaka'})
    app.builder.build_all()
    assert app.config.sphinxmark_image == 'text'
    assert app.config.sphinxmark_text == 'Mitaka'

    html = (app.outdir / htmlfile).read_text()
    assert htmlresult in html

    css = (app.outdir / cssfile).read_text()
    assert ('url("textmark_Mitaka.png")') in css


def test_image():
    """Test image."""
    image = 'new.png'
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': image})
    app.builder.build_all()
    assert app.config.sphinxmark_image == image

    html = (app.outdir / htmlfile).read_text()
    assert htmlresult in html

    css = (app.outdir / cssfile).read_text()
    cssresult = 'url("%s")' % image
    assert cssresult in css


@xfail(raises=IOError)
def test_imagefail():
    """Test image not found."""
    # ------------------ THIS SHOULD FAIL ------------------
    image = 'fail.png'
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': image})
    app.builder.build_all()
    assert app.config.sphinxmark_image == image

    html = (app.outdir / htmlfile).read_text()
    assert htmlresult in html

    css = (app.outdir / cssfile).read_text()
    cssresult = 'url("%s")' % image
    assert cssresult in css


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

    html = (app.outdir / htmlfile).read_text()
    assert htmlresult in html

    css = (app.outdir / cssfile).read_text()
    cssresult = 'url("%s")' % image
    assert cssresult in css


@xfail(raises=IOError)
def test_staticfail():
    """Test static not found."""
    # ------------------ THIS SHOULD FAIL ------------------
    image = 'new.png'
    htmlpath = ['static']
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': image,
                                 'html_static_path': htmlpath})
    app.builder.build_all()
    assert app.config.sphinxmark_image == image
    assert app.config.html_static_path == htmlpath

    html = (app.outdir / htmlfile).read_text()
    assert htmlresult in html

    css = (app.outdir / cssfile).read_text()
    cssresult = 'url("%s")' % image
    assert cssresult in css


def test_div():
    """Test div."""
    app = MakeApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_div': 'body-test'})
    app.builder.build_all()
    assert app.config.sphinxmark_div == 'body-test'

    html = (app.outdir / htmlfile).read_text()
    assert htmlresult in html

    css = (app.outdir / cssfile).read_text()
    assert ('div.body-test') in css


if __name__ == '__main__':
    pass
