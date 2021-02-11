==============
OfficiumDivium
==============

OfficiumDivinum is a modern re-write of
https://divinumofficium.com. It provides a REST-like (hopefully
RESTful) API to get the office and the mass in html, serialised json,
latex or gabc, suitable not just for reading but also for singing.

We provide an API and a demonstration web app: you go and build the rest!

Using the Web API
-----------------

Get tomorrow’s martyrology as json:

.. code:: bash

   curl -H "Accept: application/json" --request GET "http://2e0byo.pythonanywhere.com:/martyrology"

Get the hymn from today’s Prime in latin in html:

.. code:: bash
	  
   curl -H "Accept: text/html" --request GET "http://2e0byo.pythonanywhere.com:/office?office=prime&lang=latin&part=hymn"

Using in your own code
----------------------

To use OfficiumDivinum in a project::

  import officiumdivinum

You probably want to import some of our structures and functions, like
this::

  from officiumdivinum import objects as off_obj

  feast = off_obj.Feast(*args) # etc

   
.. toctree::
   :maxdepth: 2

   background
   installation
   reference/index
   contributing
   authors
   changelog

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
