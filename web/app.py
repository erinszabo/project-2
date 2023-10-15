"""
Erin Szabo's Flask API.
"""

from flask import Flask, abort, send_from_directory
import config

app = Flask(__name__)


@app.route("/")
def hello():
    return "UOCIS docker demo!\n"

# return abort(403) to use this
@app.errorhandler(403)
def forbidden(e):
    return send_from_directory(root, '403.html'), 403

@app.errorhandler(404)
def notfound(e):
    return send_from_directory(root, '404.html'), 404

@app.route("/<string:file>")
def filecheck(file):
    if ".." in file or "~" in file:
        return abort(403)
    return send_from_directory(root, file), 200


if __name__ == "__main__":
    options = config.configuration()
    root = options.DOCROOT
    port = options.PORT

    app.run(debug=True, host='0.0.0.0', port=port)
