import os
from flask import Flask, render_template, request
from flask_dropzone import Dropzone

app = Flask(__name__)
dropzone = Dropzone(app)
thisDir = os.path.dirname(__file__)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file')
    f.save("%s/static/%s" % (thisDir, f.filename))
    return "OK"


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
