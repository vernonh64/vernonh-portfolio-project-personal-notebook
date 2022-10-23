#app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
 
app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads/'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
path = "static/uploads"
dir_list = os.listdir(path) 
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
 
@app.route('/')
def home():
       dir_list = os.listdir(path)
       return render_template('index.html', file_list=dir_list)
 
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        dir_list = os.listdir(path) 
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename,  file_list=dir_list)
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    dir_list = os.listdir(path)
    return redirect(url_for('static', filename='uploads/' + filename), code=301,  file_list=dir_list)
 
@app.route('/test')
def test():
    flash('triggered on click')
    print ("Hello")
    #return render_template
 
if __name__ == "__main__":
    app.run()