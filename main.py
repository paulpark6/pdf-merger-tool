import os
from methods import merge_pdfs_with_titles

if __name__ == "__main__":
    print("--- PDF Merger with Title Pages ---")

    # 1. Get the folder path from user input
    # .strip() removes spaces
    # .strip('\'"') removes both single and double quotes from start/end
    folder_path = input("Enter the path to the folder containing PDFs: ").strip().strip('\'"')

    # Simple validation loop to ensure folder exists
    while not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' was not found.")
        folder_path = input("Please enter a valid folder path: ").strip().strip('\'"')

    # 2. Get the output filename (Optional)
    output_name = input("Enter name for the merged file (press Enter for 'merged_output.pdf'): ").strip()
    
    # Set default if user pressed Enter
    if not output_name:
        output_name = "merged_output.pdf"
    
    # Ensure the filename ends with .pdf
    if not output_name.lower().endswith('.pdf'):
        output_name += ".pdf"

    # 3. Run the function
    print(f"\nProcessing files in: {folder_path}")
    merge_pdfs_with_titles(folder_path, output_name)