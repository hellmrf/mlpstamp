"""Test pre-gen hook in extensions are available and exposed methods are callable."""

import sys

if '{% hello mlpstamps.name %}' == 'Hello Cookiemonster!':
    sys.exit(0)
else:
    sys.exit(1)
