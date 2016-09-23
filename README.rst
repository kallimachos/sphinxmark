==========
sphinxmark
==========

.. image:: https://travis-ci.org/kallimachos/sphinxmark.svg?branch=master
   :target: https://travis-ci.org/kallimachos/sphinxmark

.. image:: https://img.shields.io/pypi/status/sphinxmark.svg?style=flat
   :target: https://pypi.python.org/pypi/sphinxmark

.. image:: https://img.shields.io/pypi/v/sphinxmark.svg?style=flat
   :target: https://pypi.python.org/pypi/sphinxmark

.. image:: https://img.shields.io/badge/Python-2.7-brightgreen.svg?style=flat
   :target: http://python.org

.. image:: https://img.shields.io/badge/Python-3.4-brightgreen.svg?style=flat
   :target: http://python.org

.. image:: http://img.shields.io/badge/license-apache-blue.svg?style=flat
   :target: http://www.apache.org/licenses/LICENSE-2.0

**sphinxmark** is an extension for Sphinx that enables watermarks for
HTML output.

Full documentation: https://kallimachos.github.io/sphinxmark/


Installation
~~~~~~~~~~~~

Install sphinxmark using pip:

.. code::

   $ pip install sphinxmark


Usage
~~~~~

#. Add sphinxmark to the list of extensions in ``conf.py``:

   .. code::

      extensions = ['sphinxmark']

#. Enable sphinxmark in ``conf.py``:

   .. code::

      sphinxmark_enable = True

#. Build your docs as normal. A DRAFT watermark now appears behind the text.

   .. note::

      Some Sphinx themes place body content in different CSS divs. See the
      `sphinxmark documentation <https://kallimachos.github.io/sphinxmark/>`_
      for full configuration details.
