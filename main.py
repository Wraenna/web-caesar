from flask import Flask, request, redirect
from caesar import rotate_string
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <!-- <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css')}}" /> -->
        <style>
            body {{
                background-color: #FFFDF8;
            }}

            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}

            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}

            .error {{
                color: red;
            }}
        </style>
    </head>
    <body>
      <form action="" method="post">
        <label for="rot">Rotate by: <input type="text" name="rot" value="0"/></label>
        <p class="error">{rot_error}</p>
        <textarea rows="4" cols="50" name="text">{text}</textarea>
        <p class="error">{text_error}</p>
        <input type="submit" />
      </form>
    </body>
</html>
"""

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/")
def index():
    return form.format(rot_error="", text="", text_error="")

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
        return form.format(rot=rot, text=text, rot_error=rot_error, text_error=text_error)
    else:
        rot = int(rot)

    if text == "":
        text_error = cgi.escape("Please enter some text to rotate.")
        text = ""
        rot = rot
        rot_error = rot_error
        return form.format(rot=rot, text=text, rot_error=rot_error, text_error=text_error)
    else:
        encrypted = rotate_string(text, rot)

    return form.format(rot="0", text=encrypted, rot_error="", text_error="")

app.run()
