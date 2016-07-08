#!/bin/python3
# coding: utf-8
"""sphinx-watermark is an extension for Sphinx that enables watermarks for
HTML output."""

from docutils import nodes


class Watermark(nodes.General, nodes.Element):
    pass


def visit_watermark_node():
    pass


def setup(app):
    app.add_config_value('enable_watermarks', False, 'html')

    app.add_node(watermark, html=(visit_todo_node, depart_todo_node))

    app.add_directive('watermark', WatermarkDirective)
    app.connect('doctree-resolved', process_watermark_nodes)
    app.connect('env-purge-doc', purge_watermarks)

    return {'version': '0.1'}   # identifies the version of our extension


if __name__ == '__main__':
    pass
