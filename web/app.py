"""
John Doe's Flask API.
"""

from flask import Flask, abort, send_from_directory, render_template
import config

app = Flask(__name__)
options = config.configuration()
root = options.DOCROOT
port = options.PORT


@app.route("/h")
def hello():
    return "UOCIS docker demo!\n"

@app.route("/")
def index():
    return send_from_directory(root, 'trivia.html')
# return send_from_directory('pages/', 'trivia.html')

if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0', port=port)
