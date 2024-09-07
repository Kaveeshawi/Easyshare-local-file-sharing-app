from flask import Flask, request, redirect, url_for, send_from_directory, render_template, flash
import os
from werkzeug.utils import secure_filename
import webbrowser
import threading

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # For session management

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 1024  # Limit file size to 1 GB

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mkv', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part', 'danger')
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No file selected', 'danger')
        return redirect(url_for('index'))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded', 'success')
        return redirect(url_for('index'))
    
    flash('File type not allowed', 'danger')
    return redirect(url_for('index'))

@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash('File successfully deleted', 'success')
    else:
        flash('File not found', 'danger')
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/rename', methods=['POST'])
def rename_file():
    old_filename = request.form['old_filename']
    new_filename = request.form['new_filename']
    
    if old_filename and new_filename:
        old_filepath = os.path.join(app.config['UPLOAD_FOLDER'], old_filename)
        new_filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(new_filename))
        
        if os.path.exists(old_filepath):
            os.rename(old_filepath, new_filepath)
            flash('File successfully renamed', 'success')
        else:
            flash('File not found', 'danger')
    else:
        flash('Invalid file names provided', 'danger')
    
    return redirect(url_for('index'))

# Flag to ensure the browser opens only once
browser_opened = False

def open_browser():
    global browser_opened
    if not browser_opened:
        print("Opening browser...")
        webbrowser.open('http://127.0.0.1:5000/')
        browser_opened = True

if __name__ == "__main__":
    # Open the default web browser to the app URL in a separate thread
    threading.Timer(2, open_browser).start()
    app.run(host='0.0.0.0', port=5000, debug=False)  # Disable debug mode for this test
