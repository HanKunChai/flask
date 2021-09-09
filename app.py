import os
from config import Config
from flask import Flask, request, Response, send_file
from flask import render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
cfg = Config()


@app.route('/')
def hello_world():
    return render_template('Uploader.html')


@app.route('/upload/<string:filename>', methods=['POST'])
def upload(filename):
    f = request.files['file']

    f.save(os.path.join(cfg.filepath, secure_filename(filename)))
    return "success"


@app.route('/delete/<string:index>', methods=['GET'])
def delete(index):
    files = os.listdir(cfg.filepath)
    try:
        os.remove(os.path.join(cfg.filepath, files[int(index)]))
    except:
        return "Delete Failed"

    return 'Success'


@app.route('/getfilenames', methods=["GET"])
def listfiles():
    files = os.listdir(cfg.filepath)
    return {'filelist': files}

@app.route('/download/<string:index>')
def download(index):
    files = os.listdir(cfg.filepath)
    file = os.path.join(cfg.filepath,files[int(index)])
    return send_file(file)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
