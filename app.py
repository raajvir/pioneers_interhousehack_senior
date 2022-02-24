import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import time

import main

# Configure application
app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["IMAGE_UPLOADS"] = "static/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


""" @app.route("/")
@login_required
def index():
    gh = create()
    rows = main.keywordreader(cat)
    rows = db.execute("SELECT * FROM users WHERE id = :user_id", user_id=session["user_id"])

    print(cat, rows)
    return render_template("index.html", stocks=rows) """


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("create.html")
    else:
        industry = str(request.form.get("industry"))
        description = str(request.form.get("desc"))
        name = str(request.form.get("name"))
        x = industry + " " + description
        rows = main.sentencekeywordreader(x)
        print(rows, x)

        return render_template('index.html', stocks=rows)


if __name__ == "__main__":
    app.run()
