#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from filehoster import db

class UploadedFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.Text, unique=True, nullable=False)
    filename = db.Column(db.Text, nullable=False)

    def __init__(self, hash, filename):
        self.hash = hash
        self.filename = filename

    def __repr__(self):
        return "<File id={0}>".format(self.id)
