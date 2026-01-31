import os
import io
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_title_page(text):
    """
    Creates a PDF page in memory with the given text centered on it.
    """
    packet = io.BytesIO()
    # Create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    width, height = letter
    
    # Set font and draw centered text
    can.setFont("Helvetica-Bold", 30)
    can.drawCentredString(width / 2, height / 2, text)
    
    can.save()
    packet.seek(0)
    return PdfReader(packet)

def merge_pdfs_with_titles(source_folder, output_filename="merged_output.pdf"):
    """
    Reads all PDFs in source_folder, creates title pages for them, 
    and merges them into a new folder named 'merged_file' inside the source directory.
    """
    writer = PdfWriter()
    
    if not os.path.exists(source_folder):
        print(f"Error: The folder '{source_folder}' does not exist.")
        return

    # --- Setup Output Directory ---
    # Create the path for the new subfolder
    output_dir = os.path.join(source_folder, "merged_file")
    
    # Create the folder if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Define the full path for the final PDF
    output_path = os.path.join(output_dir, output_filename)

    # --- Get Files ---
    # We only look for files in the main source_folder (not recursive)
    files = [f for f in os.listdir(source_folder) if f.lower().endswith('.pdf')]
    files.sort() 

    if not files:
        print("No PDF files found in the folder.")
        return

    print(f"Found {len(files)} files. Merging...")

    for filename in files:
        file_path = os.path.join(source_folder, filename)
        
        # --- Step 1: Create and add the Title Page ---
        title = f"Start of: {filename}"
        title_pdf_reader = create_title_page(title)
        writer.add_page(title_pdf_reader.pages[0])
        
        # --- Step 2: Add the actual PDF content ---
        try:
            reader = PdfReader(file_path)
            for page in reader.pages:
                writer.add_page(page)
            print(f"Added: {filename}")
        except Exception as e:
            print(f"Could not read {filename}: {e}")

    # --- Step 3: Write the final file ---
    try:
        with open(output_path, "wb") as out_file:
            writer.write(out_file)
        print(f"\nSuccess! Merged PDF saved to: {output_path}")
    except PermissionError:
        print(f"\nError: Could not save to {output_path}. Is the file open?")