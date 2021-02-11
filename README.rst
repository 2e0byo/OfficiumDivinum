========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls|
        | |codacy|
    * - package
      - | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/OfficiumDivinum/badge/?style=flat
    :target: https://readthedocs.org/projects/OfficiumDivinum
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.com/OfficiumDivinum/OfficiumDivinum.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.com/github/OfficiumDivinum/OfficiumDivinum

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/OfficiumDivinum/OfficiumDivinum?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/OfficiumDivinum/OfficiumDivinum

.. |requires| image:: https://requires.io/github/OfficiumDivinum/OfficiumDivinum/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/OfficiumDivinum/OfficiumDivinum/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/github/OfficiumDivinum/OfficiumDivinum/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://coveralls.io/github/OfficiumDivinum/OfficiumDivinum?branch=master

.. |codacy| image:: https://img.shields.io/codacy/grade/93ba847130a24c3eb555404b8df8f74d.svg
    :target: https://www.codacy.com/app/OfficiumDivinum/OfficiumDivinum
    :alt: Codacy Code Quality Status

.. |commits-since| image:: https://img.shields.io/github/commits-since/OfficiumDivinum/OfficiumDivinum/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/OfficiumDivinum/OfficiumDivinum/compare/v0.0.0...master



.. end-badges

An Object-Oriented rewrite of divinumofficium.com.

* Free software: MIT license

Installation
============

If you want the latest release::
  
   python -m pip install https://github.com/OfficiumDivinum/OfficiumDivinum/archive/master.zip
    
You can also install the in-development version with::

  python -m pip install git+https://github.com/OfficiumDivinum/OfficiumDivinum

If you want to develop (or just tinker), [fork and] clone the
repository, and then install in ‘development mode’::

  git clone https://github.com/OfficiumDivinum/OfficiumDivinum
  cd OfficiumDivinum
  python -m venv venv # create a virtual environment
  source venv/bin/activate # if using bash
  # . venv/bin/activate.fish # if using fish
  python -m pip install -e .

To run the development server, run::

  export FLASK_APP=src/api.py
  export FLASK_ENV=developemnt
  flask run


Documentation
=============


https://OfficiumDivinum.readthedocs.io/

Background
----------

Divinumofficium is incredible.  Unfortunately, it is hard to know how
it works:

* Some data is stored in various (not really documented) text files,
  other is hard-coded into scripts.
* Some things are in funny places (for instance, the feast of the Holy
  Name of Jesus is assigned in the calendar to the ‘0th January’, and
  then moved to its variable date by the code).
* Perl is very hard to read, at least for non perl coders!
* Functions call each other in fun and non-obvious ways (at least for
  non perl coders!)
* It’s basically stateless, and takes the /Divinum Afflatu/ version as
  the ‘default’, then to mutate it.  But this occasionally has problems.

And it is hard to extend it:

* The database format (which in any case is not used for everything)
  is basically designed to output plaintext.
* There are no symbolic representations of e.g. days, psalms, chapters
  which could be traded for e.g. `gabc`. files to generate scores to
  sing from.
* Perl is hard!  (Did I say that before?)

OfficiumDivinum is an attempt to address these problems by a complete
re-write in a more modern idiom.  For a thorough rationale and
philosophy (in the sense of ‘policy’ ;)) of the new approach see
`background <https://OfficiumDivinum.readthedocs.io/background>`_.

Using it
--------

You probably just want to go to the
`documentation <https://OfficiumDivinum.readthedocs.io>`_ and start
using the web API.  But you might want to build a local service.  In
the future there will be apps for Android and iOS.


Development
===========

To run all the tests and build documentation, run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
