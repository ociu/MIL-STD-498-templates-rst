MIL-STD-498 templates
=====================

MIL-STD-498 DID templates in [reStructuredText](http://docutils.sourceforge.net/rst.html) format.

These templates are a good starting point for documenting a software project.

reStructuredText is the format used in official
[Python documentation](http://docs.python.org).
It is supported by 
[docutils](http://docutils.sourceforge.net/), 
[Sphinx](http://sphinx-doc.org/), 
[Read The Docs](https://readthedocs.org/)
and many wiki engines, and can be actually converted to the most popular document formats.

Original files in Markdown format taken from https://github.com/bradfa/MIL-STD-498.
Appart from format conversion, other changes performed:

- Set DID name as document title

- Removed dots at the end of sections

- Removed section numbers (left to user's decission; docutils can generate them)

- Guidance paragraphs converted to rst comments. So you don't have to remove them when you create content,
  they are always generated as comments also in the target format.
