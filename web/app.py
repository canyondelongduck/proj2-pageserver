from flask import Flask, render_template, abort
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "UOCIS docker demo!"

@app.errorhandler(404)
def handle_404(i):
    return render_template("404.html"), 404

@app.errorhandler(403)
def handle_403(i):
    return render_template("403.html"), 403

@app.route("/<path:filename>")
def serve_file(filename):
    if "~" in filename or "//" in filename or ".." in filename:
        return abort(403)
    full_path = os.path.join("templates", filename)
    if os.path.isfile(full_path):
        return render_template(filename)
    return abort(404)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
