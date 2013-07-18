# Markdown to reStructuredText MIL-STD-498 conversion script
#
# Usage: cat origin.md | python convert.py "Document Title" > target.rst
#

import fileinput
import sys
import re

# Constants to assign to ``previous`` variable
TITLE = 1
EMPTY = 2
TEXT = 3

# rst sections characters: up to depth level 7, Emacs style
section_char = ['=', '=','-','~','+','`','#','@']
previous = EMPTY

# Print document title
print section_char[0] * (len(sys.argv[1]) + 2)
print "", sys.argv[1]
print section_char[0] * (len(sys.argv[1]) + 2)

# Print directives
print """
.. contents:: Table of Contents
.. sectnum::
"""

# Read from stdin and convert to stdout
for line in fileinput.input('-'):
    
    section = re.match(r'^(#+)\s+\S*\s+(.*)\.', line)

    # md sections to rst
    if section:
        section_depth = len(section.group(1))
        section_title = section.group(2)

        print '\n', section_title
        print section_char[section_depth] * len(section_title)
        previous = TITLE

    # Text to comments
    else:
        if len(line) > 1:
            if previous != TEXT:
                print "..", line,
            else:
                print "  ", line,
            previous = TEXT
        else:
            print
            previous = EMPTY
