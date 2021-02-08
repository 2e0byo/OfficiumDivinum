.. Officium Divinum documentation master file, created by
   sphinx-quickstart on Fri Jan 29 22:00:33 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

*Officium Divinum*: an object-oriented divinumofficium
======================================================

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   rationale
   contributing
   source/modules

*OfficiumDivinum* is an object-oriented re-write of divinum
officium.  For why we attempted this, see :doc:`rationale`.

*OfficiumDivinum* provides:

* A REST-like (hopefully RESTful) API to serve both *objects* (hymns,
  psalms, ordo for a given day) and complete *products* (‘today’s
  vespers as a latex file with all chant in gabc’, ‘today’s lauds as
  an html file’.)
* Objects and structures to describe the kind of things used in
  liturgical texts (hymns, psalms, versicle, etc), together with
  reusable renderers for them, all based around jinja templates.
* Rubrical and Calendrical rules implemented as classes with standard
  methods, derived from a basic human-readable DSL.
* Data in human-readable format, editable by non-programmers.

It endeavours:

* To provide all the functionality of https://divinumofficium.com as a
  demo web app.
* To provide a fully-documented API to encourage the development of
  apps, websites, programs *etc* for the praying of the Divine Office
  in the Ancient Rite(s) of the Western Church.
* To be easy to contribute to, particularly by non-programmers.  To
  this end we have striven entirely to abstract the liturgical texts
  and rubrics from the code which implements them.
* To be flexible enough to support any plausible calendar or set of
  rubrics, ancient or modern.
* To provide Local Calendars.
* To encourage the public and private reciting, singing and study of
  the Divine Office.

If you would like to contribute, see :doc:`contributing` to get
started.  

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
