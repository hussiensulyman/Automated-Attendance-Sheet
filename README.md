# Automated Attendance Sheet

A Flask-based web application for automating attendance tracking using facial recognition, built with OpenCV and face_recognition. This project demonstrates backend development skills, including image processing, Flask routing, and SQLite integration, suitable for a university attendance system.

## Features
- Automates attendance by recognizing faces in uploaded images.
- Stores attendance records in `sample_attendance.csv` and a SQLite database.
- Includes `sample_dataset/` with non-sensitive images for testing.
- Excludes sensitive student data (e.g., original images, encodings) for privacy compliance.
- Responsive web interface for uploading images and viewing attendance reports.

## Prerequisites
- Python 3.8 or higher
- Build tools for `dlib` (e.g., CMake, Visual Studio on Windows, `libopenblas-dev` on Linux)
- Git for cloning the repository

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/hussiensulyman/Automated-Attendance-Sheet.git
   cd Automated-Attendance-Sheet
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open `http://127.0.0.1:5000` in a browser.

## Usage
1. Navigate to the web interface (`http://127.0.0.1:5000`).
2. Upload an image from `sample_dataset/` (e.g., `person1.jpg`) via the upload form.
3. View recognized names and timestamps in the attendance table.
4. Check `sample_attendance.csv` for updated records (format: `name,id,timestamp`).
5. Note: Original student data is excluded; use `sample_dataset/` for testing.

## Project Structure
```
Automated-Attendance-Sheet/
├── app.py                          # Main Flask application
├── face_recognition_utils.py       # Facial recognition utilities
├── predict.py                      # Attendance prediction logic
├── face detection then recognition model without gui.py  # Core recognition model
├── final project.py                # Alternative implementation (optional)
├── cascades/                       # Haar cascade files for face detection
├── sample_dataset/                 # Non-sensitive test images
├── sample_attendance.csv           # Sample attendance records
├── templates/                      # HTML templates for web interface
├── static/                         # CSS/JavaScript for styling
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── LICENSE                         # MIT License
├── .gitignore                      # Ignored files (e.g., venv/, Attendance.csv)
```

## Testing
- Use images in `sample_dataset/` (e.g., `person1.jpg`, `person2.jpg`) to test recognition.
- Ensure `sample_attendance.csv` updates with entries like `Person1,001,2025-05-01 10:00`.
- Run `python app.py` and test uploads via the web interface.

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Contact
- GitHub: [hussiensulyman](https://github.com/hussiensulyman)
- Email: [hussiensulyman@gmail.com] (hussiensulyman@gmail.com)

## License
MIT License
