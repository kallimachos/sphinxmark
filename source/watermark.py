#!/bin/python3
# coding: utf-8
"""A Sphinx extension that enables watermarks for HTML output."""

import os


def watermark(app, env):
    """Add watermark."""
    if app.builder.format == 'html':
        path = os.path.join(app.builder.outdir, 'myawesomefile')
        open(path, 'wt').close()


def setup(app):
    """Setup for Sphinx ext."""
    app.add_config_value('watermark_enable', False, 'html')
    app.add_config_value('watermark_image', 'watermark-draft.png', 'html')
    app.connect('env-updated', watermark)
    return {'version': '0.1'}


if __name__ == '__main__':
    pass
