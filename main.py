from flask import Flask, request
from caesar import rotate_string

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
        </style>
    </head>
    <body>
      <form action="" method="post">
        <label for="rot">Rotate by: <input type="text" name="rot" value="0"/></label>
        <textarea rows="4" cols="50" name="text">{0}</textarea>
        <input type="submit" />
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']

    encrypted = rotate_string(text, rot)
    return form.format(encrypted)

app.run()
