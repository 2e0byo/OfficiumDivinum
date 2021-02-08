============
Contributing
============

We welcome contributions by anyone who can make the content or
implementation better in any way, or who wants to add a feature we
don’t currently provide.  If you have just found a problem or typo you
probably want to `open an issue
<https://github.com/OfficiumDivinum/OfficiumDivinum/issues>`_.

As a non-programmer
===================

OfficiumDivinum is written to be accessible to non-programmers.  In
the production version, you will be able to create an account and
edit/add all parts of the office without writing a line of code.  This
is built on our heavy use of human-readable DSLs to describe different
parts of the data.

Bug reports
===========

Bugs occur when you don’t get what you should have.  There are other
kinds of issues, see below.  When `reporting a bug
<https://github.com/OfficiumDivinum/OfficiumDivinum/issues>`_ please
include:

    * Your operating system name and version (if you are running locally).
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.
    * If you are reporting a discrepancy against published liturgical
      books, please provide a link to a pdf of to volume in question
      (there are lots of breviaries/missals on https://archive.org ).


Other kinds of Issues
=====================

Feel free to open issues to discuss the future direction of the
project; to propose changes; to tell us what you’ve done with
OfficiumDivinum, or for any other sensible reason.  You can also get
in touch by email.

Documentation improvements
==========================

OfficiumDivinum could always use more documentation, whether as part
of the official OfficiumDivinum docs, in docstrings, or even on the
web in blog posts, articles, and such.

Feature requests and feedback
=============================

The best way to send feedback is to file an issue at https://github.com/OfficiumDivinum/OfficiumDivinum/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that code contributions are welcome :)
  
Development
===========

To set up `OfficiumDivinum` for local development:

1. Fork `OfficiumDivinum <https://github.com/OfficiumDivinum/OfficiumDivinum>`_
   (look for the "Fork" button).
2. Clone your fork locally::

    git clone git@github.com:YOURGITHUBNAME/OfficiumDivinum.git

3. Create a branch for local development::

    git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

4. When you're done making changes run all the checks and docs builder with `tox <https://tox.readthedocs.io/en/latest/install.html>`_ one command::

    tox

5. Commit your changes and push your branch to GitHub::

    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature

6. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

If you need some code review or feedback while you're developing the code just make the pull request.

For merging, you should:

1. Include passing tests (run ``tox``) [1]_.
2. Update documentation when there's new API, functionality etc.
3. Add a note to ``CHANGELOG.rst`` about the changes.
4. Add yourself to ``AUTHORS.rst``.

.. [1] If you don't have all the necessary python versions available locally you can rely on Travis - it will
       `run the tests <https://travis-ci.com//github/OfficiumDivinum/OfficiumDivinum/pull_requests>`_
       for each change you add in the pull request.

       It will be slower though ...

Tips
----

To run a subset of tests::

    tox -e envname -- pytest -k test_myfeature

To run all the test environments in *parallel*::

    tox -p auto
