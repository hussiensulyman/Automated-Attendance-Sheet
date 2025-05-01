# Data Usage Policy

This document outlines how data is handled in the **Automated Attendance Sheet** project, a Flask-based web application for automating attendance tracking using facial recognition. It ensures transparency, privacy compliance, and ethical data practices for contributors and users.

## Overview
The project uses facial recognition (via OpenCV and `face_recognition`) to identify individuals in images and log attendance in a CSV file and SQLite database. To protect privacy, sensitive data (e.g., real student images, attendance records) is excluded, and only non-sensitive test data is included in the repository.

## Types of Data
1. **Images**:
   - **Purpose**: Used for facial recognition to identify individuals.
   - **Storage**: Uploaded images are temporarily stored in the `Uploads/` folder (not tracked by Git) and deleted after processing.
   - **Test Data**: The `sample_dataset/` folder contains non-sensitive images (e.g., `person1.jpg`, `person2.jpg`) generated from public sources like [ThisPersonDoesNotExist.com](https://thispersondoesnotexist.com/) for testing.
   - **Sensitive Data**: Original student images (e.g., in `Image_Attendance/`, `vision/`) are excluded via `.gitignore` and not included in the repository.

2. **Attendance Records**:
   - **Purpose**: Logs recognized names, IDs, and timestamps.
   - **Storage**: Stored in `sample_attendance.csv` (format: `name,id,timestamp`) and a SQLite database (not tracked by Git).
   - **Test Data**: `sample_attendance.csv` contains dummy entries (e.g., `Person1,001,2025-05-01 10:00`) for testing.
   - **Sensitive Data**: Original attendance records (e.g., `Attendance.csv`) are excluded via `.gitignore`.

3. **Face Encodings**:
   - **Purpose**: Numerical representations of faces for recognition.
   - **Storage**: Stored in `sample_encodings.pkl` (not tracked by Git) for testing.
   - **Sensitive Data**: Original encodings (e.g., `face_encodings.pickle`, `encodings.pkl`) are excluded via `.gitignore`.

4. **Database**:
   - **Purpose**: Stores attendance data for persistence.
   - **Storage**: SQLite database file (e.g., `attendance.db`) is not tracked by Git.
   - **Test Data**: Contributors can create a test database using `sample_dataset/`.

## Privacy and Security Practices
- **No Sensitive Data in Repository**: All sensitive data (e.g., student images, real attendance records, face encodings) is excluded via `.gitignore` to comply with privacy standards.
- **Temporary File Handling**: Uploaded images are deleted after processing (see `app.py`) to prevent persistent storage.
- **Non-Sensitive Test Data**: The repository includes `sample_dataset/` and `sample_attendance.csv` with dummy data for testing, ensuring no real individuals are referenced.
- **No External Storage**: Data is not sent to external servers or cloud services; all processing occurs locally.
- **Secure Dependencies**: The project uses vetted libraries (e.g., `face_recognition`, `Flask`) listed in `requirements.txt`.

## Guidelines for Contributors
To maintain privacy and ethical standards, contributors should:
1. **Use Test Data Only**:
   - Test the application with images in `sample_dataset/` or generate new non-sensitive images (e.g., via [ThisPersonDoesNotExist.com](https://thispersondoesnotexist.com/)).
   - Do not include real student data or sensitive images in pull requests.
2. **Respect .gitignore**:
   - Ensure sensitive files (e.g., `Attendance.csv`, `face_encodings.pickle`, `Uploads/`) remain excluded.
   - Add new sensitive files to `.gitignore` if created (e.g., `test_venv/`).
3. **Handle Data Securely**:
   - Delete temporary files (e.g., uploaded images) after testing.
   - Avoid logging sensitive data in debug outputs or logs.
4. **Update Documentation**:
   - If adding new data types (e.g., new CSV formats), update this `data-usage.md` file.
   - Document any new test data in `README.md` or `sample_dataset/`.

## Legal and Licensing
- The project is licensed under the [MIT License](LICENSE), which governs the use of code and included test data (e.g., `sample_dataset/`, `sample_attendance.csv`).
- Contributors are responsible for ensuring any new data added complies with applicable privacy laws (e.g., GDPR, FERPA) and does not include personal information.
