#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/wsgi-scripts/myapp/")

from app import app
app.secret_key = 'Add your secret key'
