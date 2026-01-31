# PDF Merger with Title Pages

A Python tool that merges multiple PDF files from a specific folder into a single document. It automatically inserts a generated title page before every file to indicate where the new document begins.

## Features
* **Smart Merging:** Combines all PDFs in a target folder.
* **Auto-Title Pages:** Generates a clean title page (e.g., "Start of: Lecture 1.pdf") before each merged section.
* **Safety:** Saves the output in a separate `merged_file` subfolder to avoid overwriting originals.
* **User Friendly:** Supports dragging and dropping folders into the terminal (handles path quotes automatically).

## Prerequisites

* Python 3.x
* `pip` (Python package manager)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/pdf-merger-tool.git](https://github.com/YOUR_USERNAME/pdf-merger-tool.git)
    cd pdf-merger-tool
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    * **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **Windows:**
        ```bash
        venv\Scripts\activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the main script:
    ```bash
    python main.py
    ```

2.  **Enter the Folder Path:**
    * When prompted, paste the path to the folder containing your PDFs.
    * *Tip:* You can drag and drop the folder from Finder/Explorer directly into the terminal window. The script automatically handles any extra quotes added by the terminal.

3.  **Enter Output Name:**
    * Type a name for the final file (e.g., `Final_Exam_Review`), or press **Enter** to use the default (`merged_output.pdf`).

4.  **Find your File:**
    * The script creates a new folder named `merged_file` inside your source directory. Your combined PDF will be saved there.

## Project Structure

* `main.py`: The entry point. Handles user input and path validation.
* `methods.py`: Contains the logic for generating title pages and merging files.
* `requirements.txt`: List of required Python libraries (`pypdf`, `reportlab`).

## Dependencies

* [pypdf](https://pypi.org/project/pypdf/) - For reading and writing PDF files.
* [reportlab](https://pypi.org/project/reportlab/) - For generating the text-based title pages on the fly.