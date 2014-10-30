#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import base64, hashlib, os
from flask import render_template, request, send_from_directory
from werkzeug import secure_filename

from filehoster import app, db
from filehoster.models import UploadedFile
from filehoster.utils import allowed_file

@app.route('/', methods=['GET'])
def index():
    return render_template("message.html", \
        message="This is not the page you're looking for. Move along.")

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == "GET":
        return render_template("upload_form.html")

    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_location) # File cursor gets moved to EOF

        file.stream.seek(0)
        filehash = hashlib.sha512(file.stream.read()).hexdigest()

        #TODO Rename file to filehash.ext to avoid collisions?

        if UploadedFile.query.filter(UploadedFile.hash==filehash).count() == 0:
            uploaded_file = UploadedFile(filehash, filename)
            db.session.add(uploaded_file)
            db.session.commit()

            return render_template("message.html", \
                 message="New File: http://web.site/{0}".format(uploaded_file.id))
        else:
            existing_file = UploadedFile.query.filter(UploadedFile.hash==filehash).first()

            return render_template("message.html", \
                message="Existing File: http://web.site/{0}".format(existing_file.id))
    return render_template("message.html", message="Upload failed!")

@app.route('/<int:image_id>/', methods=['GET'])
def get_file(image_id):
    file = UploadedFile.query.get(image_id)
    if not file:
        return render_template("message.html", message="Unknown ID!")
    return send_from_directory(app.config['UPLOAD_FOLDER'], file.filename)
