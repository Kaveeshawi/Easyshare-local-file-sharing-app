# Easyshare Local File Share App

Easyshare is a simple Flask-based web application for local file sharing. It allows users to upload, view, download, rename, and delete files. This application supports various file types, including text files, PDFs, images, and video formats.

## Features

- **Upload Files**: Supports multiple file types including `.txt`, `.pdf`, `.png`, `.jpg`, `.jpeg`, `.gif`, `.mp4`, `.mkv`, `.mov`.
- **View Uploaded Files**: Lists all uploaded files with options to download or delete them.
- **Rename Files**: Allows renaming of uploaded files.
- **Delete Files**: Option to delete files from the server.

## Prerequisites

- Python 3.x
- Flask
- werkzeug

## Installation

1. **Clone the repository:**

    ```bash
   git clone https://github.com/Kaveeshawi/Easyshare.git
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Create the `uploads` directory:**

    Ensure the `uploads` folder exists or create it:

    ```bash
    mkdir uploads
    ```

## Configuration

- **`app.py`**: Main application file.
- **`templates/`**: Contains the HTML templates, specifically `index.html`.

## Running the Application

1. **Start the Flask application:**

    ```bash
    python app.py
    ```

2. **Access the application in your web browser:**

    Open your browser and go to `http://127.0.0.1:5000/` or the local DNS name you have set up.

## Usage

- **Upload a File**: Select a file and click the "Upload" button.
- **View Files**: Uploaded files will be displayed with options to download or delete.
- **Rename a File**: Enter the current file name and the new name to rename a file.
- **Delete a File**: Click the trash icon next to the file to delete it.

## Notes

- Ensure that the `UPLOAD_FOLDER` is correctly set and has appropriate permissions for file operations.
- Adjust `MAX_CONTENT_LENGTH` in `app.py` if needed for larger files.

## Troubleshooting

- If you encounter an error, check the console output for details.
- Make sure Flask and the required packages are correctly installed.

## Contact

For any issues or inquiries, please contact [my email](mailto:kaveeshawi@gmail.com).

## License

Copyright © 2024 Kaveesha Wijesiriwardana
