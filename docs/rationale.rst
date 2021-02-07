Rationale
=========

History: Divinumofficium
========================

Divinumofficium is an incredible achievement: it presents the complete
divine office and missal of the Roman rite from its Tridentine form
through to its currently authorised version (‘rubrics 1960’), as well
as a ‘monastic’ office and now the Dominican breviary.  It does this
with a collection of perl scripts parsing a text-based homegrown
database structure and outputting html to STDOUT which is then
served.  That something so complicated was concieved and put together
by one man is incredible.  Unfortunately, it is hard to know how it
works:

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
  which could be traded for e.g. .gabc files to generate scores to
  sing from.  This goes for the output too: nothing is wrapped in
  classes, very little is in paragraph tags---it’s a nightmare to
  scrape!.
* Perl is hard!  (Did I say that before?)

OfficiumDivinum is an attempt to address these problems by a complete
re-write in a more modern idiom.  But none of this could have happened
had Laszlo Kiss not written the original http://divinumofficium.com,
and had others not contributed an enormous amount of material to the
divinumofficium project (as well as releasing everything over which
they had copyright under the MIT License).

History: OfficiumDivinum
========================

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
