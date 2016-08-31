#!/bin/python3
# coding: utf-8
"""Sphinxmark test file."""

from pytest import mark
from sphinx_testing import TestApp

xfail = mark.xfail


def test_defaults():
    """Test defaults."""
    app = TestApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True)
    app.builder.build_all()
    html = (app.outdir / 'index.html').read_text()
    css = (app.outdir / '_static/sphinxmark.css').read_text()
    assert ('<link rel="stylesheet" ' +
            'href="_static/sphinxmark.css" type="text/css" />') in html
    assert ('url("watermark-draft.png")') in css


def test_textmark():
    """Test textmark."""
    app = TestApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': 'text',
                                 'sphinxmark_text': 'Mitaka'})
    app.builder.build_all()
    html = (app.outdir / 'index.html').read_text()
    css = (app.outdir / '_static/sphinxmark.css').read_text()
    assert ('<link rel="stylesheet" ' +
            'href="_static/sphinxmark.css" type="text/css" />') in html
    assert ('url("textmark_Mitaka.png")') in css


def test_image():
    """Test image."""
    app = TestApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': 'new.png'})
    app.builder.build_all()
    html = (app.outdir / 'index.html').read_text()
    css = (app.outdir / '_static/sphinxmark.css').read_text()
    assert ('<link rel="stylesheet" ' +
            'href="_static/sphinxmark.css" type="text/css" />') in html
    assert ('url("new.png")') in css


@xfail
def test_imagefail(capsys):
    """Test image."""
    # ------------------ THIS SHOULD FAIL ------------------
    app = TestApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': 'fail.png'})
    app.builder.build_all()
    html = (app.outdir / 'index.html').read_text()
    css = (app.outdir / '_static/sphinxmark.css').read_text()
    assert ('<link rel="stylesheet" ' +
            'href="_static/sphinxmark.css" type="text/css" />') in html
    assert ('url("fail.png")') in css
    out, err = capsys.readouterr()
    assert err == 'hello'


def test_myoutput(capsys):
    """Temp test function for error streams."""
    print("hello")
    import sys
    sys.stderr.write("world\n")
    out, err = capsys.readouterr()
    assert out == "hello\n"
    assert err == "world\n"
    print("next")
    out, err = capsys.readouterr()
    assert out == "next\n"


@xfail
def test_imagefail2():
    """Test image."""
    # ------------------ THIS SHOULD FAIL ------------------
    app = TestApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_image': 'fail.png'})
    app.builder.build_all()
    html = (app.outdir / 'index.html').read_text()
    css = (app.outdir / '_static/sphinxmark.css').read_text()
    assert ('<link rel="stylesheet" ' +
            'href="_static/sphinxmark.css" type="text/css" />') in html
    assert ('url("bob.png")') in css


@xfail
def test_static():
    """Test static."""
    # ------------------ THIS SHOULD FAIL ------------------
    app = TestApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'html_static_path': ['static'],
                                 'sphinxmark_image': 'new.png'})
    app.builder.build_all()
    html = (app.outdir / 'index.html').read_text()
    css = (app.outdir / '_static/sphinxmark.css').read_text()
    assert ('<link rel="stylesheet" ' +
            'href="_static/sphinxmark.css" type="text/css" />') in html
    assert ('url("new.png")') in css


@xfail
def test_div():
    """Test div."""
    # ------------------ THIS SHOULD FAIL ------------------
    app = TestApp(srcdir='tests/marktest', copy_srcdir_to_tmpdir=True,
                  confoverrides={'sphinxmark_div': 'docs-body'})
    app.builder.build_all()
    html = (app.outdir / 'index.html').read_text()
    css = (app.outdir / '_static/sphinxmark.css').read_text()
    assert ('<link rel="stylesheet" ' +
            'href="_static/sphinxmark.css" type="text/css" />') in html
    assert ('url("watermark-draft.png")') in css


if __name__ == '__main__':
    pass
