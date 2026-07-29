from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from s3_config import s3, UPLOAD_BUCKET
import uuid

app = Flask(__name__)

ALLOWED_EXTENSIONS = {"log"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():

    name = request.form.get("name")
    email = request.form.get("email")
    report_format = request.form.get("report_format")

    if "logFile" not in request.files:
        return render_template(
            "error.html",
            message="No log file was uploaded."
        )

    file = request.files["logFile"]

    if file.filename == "":
        return render_template(
            "error.html",
            message="Please select a .log file."
        )

    if not allowed_file(file.filename):
        return render_template(
            "error.html",
            message="Only .log files are allowed."
        )

    filename = secure_filename(file.filename)
    unique_filename = f"incoming/{uuid.uuid4()}_{filename}"

    s3.upload_fileobj(
    Fileobj=file,
    Bucket=UPLOAD_BUCKET,
    Key=unique_filename
)

    return render_template(
    "success.html",
    name=name,
    email=email,
    filename=unique_filename,
    report_format=report_format.upper()
)


@app.route("/error")
def error():
    return render_template(
        "error.html",
        message="Something went wrong."
    )


if __name__ == "__main__":
    app.run(debug=True)