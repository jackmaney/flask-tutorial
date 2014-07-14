#!/usr/bin/env python
from app import app
import sys

debug = False

if "--dev" in sys.argv:
    debug = True

app.run(debug=debug)
