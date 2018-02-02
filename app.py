from celery_tasks import send_async_message

from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv
import os

# Load variables from .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        url = request.form.get("url")
        messagetype = request.form.get("messagetype")
        subject = request.form.get("subject")
        send_datetime = request.form.get("datetime")
        message = request.form.get("messagetext")

        # Server-side validation
        if not (url and messagetype and send_datetime and message):
            flash("Please fill out all fields")

        elif messagetype == "inmail" and not subject:
            flash("Please add a subject for your InMail")

        elif datetime < datetime.now():
            flash("Please enter a valid date and time")

        else:
            time_delay = (datetime.strptime(send_datetime, "%Y-%m-%dT%H:%M") - datetime.now()).total_seconds()
            send_async_message.apply_async(args=[url, messagetype, subject, message], countdown=time_delay)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
