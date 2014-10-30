#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from filehoster import app

# http://flask.pocoo.org/docs/0.10/patterns/fileuploads/
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
