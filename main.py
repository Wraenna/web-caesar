from flask import Flask, request, redirect, render_template
from caesar import rotate_string
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/")
def index():
    return render_template('caesar.html', title="Web Caesar", rot_error="", text="", text_error="")

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot_error = ""

    text = request.form['text']
    text_error = ""

    if not is_integer(rot):
        rot_error = cgi.escape("Please enter a numerical value.")
        rot = "0"
        text = text
        text_error = ""
        return render_template('caesar.html', title="Web Caesar", rot=rot, text=text, rot_error=rot_error, text_error=text_error)
    else:
        rot = int(rot)

    if text == "":
        text_error = cgi.escape("Please enter some text to rotate.")
        text = ""
        rot = rot
        rot_error = rot_error
        return render_template('caesar.html', title="Web Caesar", rot=rot, text=text, rot_error=rot_error, text_error=text_error)
    else:
        encrypted = rotate_string(text, rot)

    return render_template('caesar.html', title="Web Caesar", rot="0", text=encrypted, rot_error="", text_error="")

app.run()
