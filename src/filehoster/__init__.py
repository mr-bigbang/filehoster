#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.debug import DebuggedApplication

app = Flask(__name__)
app.config.from_pyfile('../config.py')

db = SQLAlchemy(app)

import filehoster.views
