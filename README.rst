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

.. |coveralls| image:: https://coveralls.io/repos/OfficiumDivinum/OfficiumDivinum/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/OfficiumDivinum/OfficiumDivinum

.. |codacy| image:: https://img.shields.io/codacy/grade/93ba847130a24c3eb555404b8df8f74d.svg
    :target: https://www.codacy.com/app/OfficiumDivinum/OfficiumDivinum
    :alt: Codacy Code Quality Status

.. |commits-since| image:: https://img.shields.io/github/commits-since/OfficiumDivinum/OfficiumDivinum/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/OfficiumDivinum/OfficiumDivinum/compare/v0.0.0...master



.. end-badges

An Object-Oriented rewrite of divinumofficium.com

* Free software: MIT license

Installation
============

::

    pip install officiumdivinum

You can also install the in-development version with::

    pip install https://github.com/OfficiumDivinum/OfficiumDivinum/archive/master.zip


Documentation
=============


https://OfficiumDivinum.readthedocs.io/


Development
===========

To run all the tests run::

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
