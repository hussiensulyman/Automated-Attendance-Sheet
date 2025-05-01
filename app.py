from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from face_recognition_utils import recognize_face
import os
from PIL import Image
import cv2
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' in request.files:
        file = request.files['image']
        if file.filename == '':
            return jsonify({'message': 'No selected file'})
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            recognized_name = recognize_face(file_path)
            return jsonify({'message': 'Image received from file upload', 'name': recognized_name})
    else:
        return jsonify({'message': 'Invalid request'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)