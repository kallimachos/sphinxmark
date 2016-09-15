====================================
Welcome to testmark's documentation!
====================================

This is an RST doc for testing the sphinxmark extension.

Contents:

.. toctree::
   :maxdepth: 2

**sphinxmark** is an extension for Sphinx that enables watermarks for
HTML output.

Full documentation: https://kallimachos.github.io/sphinxmark/


Usage
~~~~~

#. Install sphinxmark:

   ``$ pip install sphinxmark``

#. Open ``conf.py`` and import sphinxmark:

   ``import sphinxmark``

#. Add watermark to the list of extensions in ``conf.py``:

   ``extensions = ['sphinxmark']``

#. Specify a static directory in ``conf.py`` for your watermark files. If the
   path does not exist, the watermark extension creates the directory and
   populates it with ``watermark.css`` and ``watermark-draft.png``:

   ``html_static_path = ['_static']``

#. Configure watermark in ``conf.py`` as required:

   ``watermark_enable = True``

#. Put images in your static directory and edit ``watermark_image``
   to use custom watermarks.


More paragraphs
~~~~~~~~~~~~~~~

Lorem ipsum dolor sit amet, per te enim fabulas invidunt, electram vulputate
cotidieque an has. Mei pericula maluisset concludaturque id, hinc quaeque
ullamcorper ei eam. Ius ne quot nihil iriure, legere alterum in cum. Cu sit
error altera eligendi, an omnes sapientem eam. Ipsum aeque in cum. Eum habeo
tacimates ut.

Ex dolorem temporibus ius. Ad commodo repudiare evertitur eam, eirmod labores
an cum. Ne lorem affert vel, atqui omnes complectitur his et. Ex pri elitr
deleniti concludaturque, te nam choro molestie necessitatibus.

Eu vis eius aliquid. Idque quidam mea at, mea eu inani dolorum consequuntur.
Dolore scribentur est eu, pro in suas aperiam consequat, tale molestie
urbanitas ei ius. Ea mollis suscipiantur nec, qui cu delenit perfecto, sea
prima sonet soleat ad. Nam ea wisi recusabo, eu probo legimus vim.

Ea vero constituam vix. Cum at aliquip vituperatoribus. Ius enim simul ne, mel
ad tantas consectetuer. Debitis delectus percipitur has no, quo ad eius eripuit
mandamus. Ne quaeque disputationi his.

Tollit mentitum vituperatoribus sea at. Cu his dicam voluptua temporibus, id
usu modus regione. Ea saperet principes abhorreant has, audiam denique
dissentiunt in eos. Te paulo soleat vituperatoribus pro, ut veri ridens vis.
Mei modus deleniti eleifend eu, veri maiorum oportere at ius, in diam facilis
nusquam ius. Ea noster omnesque recusabo mei, te utamur commune omnesque pri,
pro ei fabellas lucilius torquatos.
