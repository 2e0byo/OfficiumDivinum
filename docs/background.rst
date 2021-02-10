.. _background:

Background
==========

OfficiumDivinum came to be when, having started an attempt to generate
LaTeX booklets from divinumofficium and given up trying to work out
how it worked (in the end I used a scraper to get the content,
although with difficulty), I (John) discovered that Endre was running
his own divinumofficium clone, with the source edited to produce
better output.  Both of us wanted something better, and I had a
working start for a rendering model, and Endre a head for
unintelligible perl (and rubrics), as well as web code.  We decided to
put together a complete re-write, as much to learn how to do it as for
the end product.

Where divinumofficium made everything bespoke and mostly unextendable,
we made wrapped everything in objects and implemented output with
rendering methods, any number of which could be created for differing
output formats.  This is very flexible, and should make building
applications around it a doddle, but it comes at the price of
conceptual complexity and cpu cycles needed to turn a DSL into
objects, solve precedences, render a bunch of objects to some output
format, and then serve that output format to a user.  We work around
this with caching, but there are certainly more efficient (if perhaps
less readable) ways to build this.

We also determined that OfficiumDivinum should be *heavily*
documented, and have a fully-functional API.


