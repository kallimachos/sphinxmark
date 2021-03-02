#!/bin/python3
# coding: utf-8
"""Sphinxmark test file."""

from os import path
from pathlib import Path

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

htmlfile = "index.html"
cssfile = "_static/sphinxmark.css"
htmlresult = f'<link rel="stylesheet" type="text/css" href="{cssfile}" />'


def test_defaults():
    """Test defaults."""
    app = MakeApp(srcdir="tests/marktest", copy_srcdir_to_tmpdir=True)
    assert app.config.sphinxmark_div == "default"
    assert app.config.sphinxmark_repeat is True
    assert app.config.sphinxmark_border is None
    assert app.config.sphinxmark_fixed is False
    assert app.config.sphinxmark_image == "default"
    assert app.config.sphinxmark_text == "default"
    assert app.config.sphinxmark_text_color == (255, 0, 0)
    assert app.config.sphinxmark_text_size == 100
    assert app.config.sphinxmark_text_width == 1000
    assert app.config.sphinxmark_text_opacity == 20
    assert app.config.sphinxmark_text_spacing == 400
    assert app.config.sphinxmark_text_rotation == 0
    app.builder.build_all()
    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html
    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ('url("watermark-draft.png")') in css


def test_div():
    """Test div."""
    app = MakeApp(
        srcdir="tests/marktest",
        copy_srcdir_to_tmpdir=True,
        confoverrides={"sphinxmark_div": "body-test"},
    )
    assert app.config.sphinxmark_div == "body-test"
    app.builder.build_all()
    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html
    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ("div.body-test") in css


def test_border():
    """Test border."""
    app = MakeApp(
        srcdir="tests/marktest",
        copy_srcdir_to_tmpdir=True,
        confoverrides={"sphinxmark_border": "left"},
    )
    assert app.config.sphinxmark_border == "left"
    app.builder.build_all()
    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html
    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ("border-left") in css


def test_repeat():
    """Text repeat."""
    app = MakeApp(srcdir="tests/marktest", copy_srcdir_to_tmpdir=True)
    assert app.config.sphinxmark_repeat is True
    app.builder.build_all()
    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html
    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ("background-repeat: repeat-y !important;") in css


def test_no_repeat():
    """Text no repeat."""
    app = MakeApp(
        srcdir="tests/marktest",
        copy_srcdir_to_tmpdir=True,
        confoverrides={"sphinxmark_repeat": False},
    )
    assert app.config.sphinxmark_repeat is False
    app.builder.build_all()
    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html
    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ("background-repeat: no-repeat !important;") in css


def test_fixed():
    """Test fixed."""
    app = MakeApp(
        srcdir="tests/marktest",
        copy_srcdir_to_tmpdir=True,
        confoverrides={"sphinxmark_fixed": True},
    )
    assert app.config.sphinxmark_fixed is True
    app.builder.build_all()
    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html
    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ("background-attachment: fixed") in css


def test_image():
    """Test image in default `_static` path."""
    image = "new.png"
    app = MakeApp(
        srcdir="tests/marktest",
        copy_srcdir_to_tmpdir=True,
        confoverrides={"sphinxmark_image": image},
    )
    assert app.config.sphinxmark_image == image
    app.builder.build_all()
    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html
    css = Path(path.join(app.outdir, cssfile)).read_text()
    cssresult = f'url("{image}")'
    assert cssresult in css


def test_imagefail():
    """Test image not found raises TypeError."""
    image = "fail.png"
    app = MakeApp(
        srcdir="tests/marktest",
        copy_srcdir_to_tmpdir=True,
        confoverrides={"sphinxmark_image": image},
    )
    assert app.config.sphinxmark_image == image
    app.builder.build_all()
    assert Path(path.join(app.outdir, cssfile)).is_file() is False


def test_textmark():
    """Test textmark."""
    app = MakeApp(
        srcdir="tests/marktest",
        copy_srcdir_to_tmpdir=True,
        confoverrides={"sphinxmark_image": "text", "sphinxmark_text": "Mitaka"},
    )
    assert app.config.sphinxmark_image == "text"
    assert app.config.sphinxmark_text == "Mitaka"
    app.builder.build_all()
    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html
    css = Path(path.join(app.outdir, cssfile)).read_text()
    assert ('url("textmark_Mitaka.png")') in css


def test_alt_static_path():
    """Test static path override."""
    image = "sample.png"
    htmlpath = ["alt_static"]
    app = MakeApp(
        srcdir="tests/marktest",
        copy_srcdir_to_tmpdir=True,
        confoverrides={"sphinxmark_image": image, "html_static_path": htmlpath},
    )
    assert app.config.sphinxmark_image == image
    assert app.config.html_static_path == htmlpath
    app.builder.build_all()
    html = Path(path.join(app.outdir, htmlfile)).read_text()
    assert htmlresult in html
    css = Path(path.join(app.outdir, cssfile)).read_text()
    cssresult = 'url("%s")' % image
    assert cssresult in css


def test_alt_static_path_fail():
    """Test static path not found raises TypeError."""
    image = "sample.png"
    htmlpath = ["fail"]
    app = MakeApp(
        srcdir="tests/marktest",
        copy_srcdir_to_tmpdir=True,
        confoverrides={"sphinxmark_image": image, "html_static_path": htmlpath},
    )
    assert app.config.sphinxmark_image == image
    assert app.config.html_static_path == htmlpath
    app.builder.build_all()
    assert Path(path.join(app.outdir, cssfile)).is_file() is False


if __name__ == "__main__":
    pass
