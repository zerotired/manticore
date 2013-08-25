:date: 2011-01-04

.. _manticore-readme:

================
Manticore README
================

.. contents::
    :depth: 2


.. include:: manticore-links.rst

.. _manticore-about:

About
=====
Manticore aims to be a blueprint for a documentation system based on Sphinx_.
Its main intention is to have an environment at your fingertips which supports
rendering reStructuredText_ documentation spread across multiple git- or
subversion-repositories.

Manticore's focus is on documentation locality (keep all your .rst files inside
the code repository they belong to), distributedness (you have some or even a lot
of repositories) and aggregation (use Sphinx_'s cross-referencing features to
interlink between documentation of different projects or artefacts).
This is achieved by standing on the shoulders of giants like git_, buildout_ and Sphinx_.

Manticore uses buildout_ along with its zerokspot.recipe.git_ and infrae.subversion_
recipes to get hold of all configured repository trees and runs the fine Sphinx_
documentation generator across them turning the reStructuredText_ documentation
into beautiful static html.

This naturally encourages developers and architects to write documentation in a very
collaborative and productive manner, even offline as there is no server or internet
access required. Everything is git-based and the documentation sources are hosted
inside the project repository you are already working on - no context switch required. :-)

On top of that, Manticore adds some nice-to-have functionality through Sphinx_ extensions
and regular Python_ code. Take a look at the :ref:`manticore-features` for details.


.. _manticore-features:

Features
========

Sphinx extensions
-----------------

- | sphinx.ext.autodoc_
  | Include documentation from docstrings.
- | sphinx.ext.viewcode_
  | Add links to highlighted source code.
- | sphinx.ext.todo_
  | Support for todo items.
- | sphinx.ext.ifconfig_
  | Include content based on configuration.
- | sphinx.ext.graphviz_
  | Add Graphviz graphs.
- | sphinx.ext.extlinks_
  | Markup to shorten external links.

- | sphinxcontrib-feed_
  | Generates a RSS feed of your site containing all articles that occur therein,
  | indexed by document date. Date is supplied as a standard document metadata field.

    .. seealso::

        :ref:`manticore-latest-edits`

- | sphinxcontrib-sdedit_, see also: `sdedit extension README`_
  | Insert sequence diagrams in your Sphinx_ document.
  | The diagrams can be authored using the `Quick Sequence Diagram Editor`_ aka. sdedit_ editor.
- | sphinxcontrib-seqdiag_ based on seqdiag_
  | Insert sequence diagrams in your Sphinx_ document.
- | sphinxcontrib-blockdiag_ based on blockdiag_
  | Insert block diagrams in your Sphinx_ document.
- | sphinxcontrib-nwdiag_ based on nwdiag_
  | Insert network diagrams into your Sphinx_ document.
- | breathe_
  | An extension to reStructuredText_ and Sphinx_ to be able to read and render Doxygen_ xml output.

Manticore addons
----------------
- ``zt.manticore.ext.changes``
    - Automatic reStructuredText_ generation of aggregated, chronological changes across all projects
    - Visualize changes using the fine `SIMILE Timeline Widget`_
- | ``zt.manticore.ext.statistics``
  | Generate repository statistics using GitStats_ and StatSVN_.
- | ``zt.manticore.ext.gource``
  | Source code repository visualization using Gource_.
- | ``zt.manticore.ext.bugseverywhere``
  | Automatic html generation of BugsEverywhere_ issues from git repositories.
- | ``zt.manticore.ext.laig``
  | "lightweight artifact interconnection grapher" based on Graphviz_


Installation
============

Get a copy of the source tree::

    git clone git@git.example.net:documentation/meta.git

Install prerequisites::

    sudo port install py-virtualenv py-docutils gnuplot

Run bootstrap and buildout as denoted below::

    virtualenv-2.7 --no-site-packages .venv27
    . .venv27/bin/activate
    pip install setuptools==0.7.2
    python bootstrap.py
    bin/buildout


.. _manticore-generate-content:

Generate content
================

To update and build all resources and artifacts, run::

    make


HTML
----

To run sphinx to generate the html output only, use::

    make html

The html output path is ``./var/sphinx``, the root page is
``./var/sphinx/index.html``. To open it, use e.g.::

    open ./var/sphinx/index.html


PDF & more
----------

``TeX`` is required to generate Latex and PDF output::

    sudo port install texlive texlive-latex-extra texlive-latex-recommended texlive-fonts-recommended

then run::

    make pdf

To open it, use e.g.::

    open ./var/latex/index.pdf


.. _manticore-add-content:

Add new content
===============

Integrate your source repository
--------------------------------

Just add a new section to ``buildout.cfg``, like:

For git repositories::

    [foobar]
    recipe = zerokspot.recipe.git
    repository = git://git.example.net/three-investigators/foobar.git
    newest = true

.. warning::
    Be aware that these git uris are used by everyone rendering the documentation,
    so you should prefer addresses using anonymous read-only access respectively
    uris that are username-agnostic.
    The main reason is not every contributor might have read-write access to all
    repositories listed.


For subversion repositories::

    [acme]
    recipe = infrae.subversion
    urls = https://svn.example.net/svn/three-investigators/acme/trunk/ .


Make sure the new section will be built by default by adding the section name
to the variable ``parts`` in section ``[buildout]``::

    [buildout]
    parts =
        foobar
        acme
        # ...


Link files into the documentation tree
--------------------------------------

Add your documents to (e.g.) ``src/index.rst``.


Use title from document (e.g.)::

    - :doc:`artefacts/foobar/docs/index`


Use custom title (e.g.)::

    - :doc:`About Foobar <artefacts/foobar/docs/index>`


.. note::

    Files **must** have the ``.rst``-suffix to be scanned and found by Sphinx.
    However, when linking into the document tree, just use the filename without suffix.



Link using labeled references
-----------------------------

Inside your reStructuredText documentation, place a reference anchor::

    .. _my-reference:

... and then link to it using::

    :ref:`my-reference`

By default, this will use the referenced section name as link title. To tweak the link title, use::

    :ref:`Custom link title <my-reference>`



Serve content via HTTP
======================


Minimal Python webserver
------------------------
You may just want to start a local Python webserver::

    cd var/sphinx; python -m SimpleHTTPServer 8668; cd -
    open http://localhost:8668/


Nginx
-----
Serve via Nginx...

Install::

    make nginx

Serve::

    bin/nginx start
    open http://localhost:8668/

Stop nginx again::

    bin/nginx stop
