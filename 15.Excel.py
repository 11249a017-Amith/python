.from PyPDF2 import PdfReader, PdfWriter

# --- List of PDFs and pages to extract ---
# Format: "filename.pdf" : [page_numbers]
# NOTE: page numbers start from 0 (0 = first page)

pdf_pages = {
    "file1.pdf": [0, 2],      # extract page 1 and 3
    "file2.pdf": [1],         # extract page 2
    "file3.pdf": [0, 1, 3]    # extract pages 1, 2, and 4
}

# Output file
output_pdf = "merged_selected_pages.pdf"
# Create a writer object
writer = PdfWriter()
# Process each PDF
for pdf_file, pages in pdf_pages.items():
    reader = PdfReader(pdf_file)
    for page_num in pages:
        if page_num < len(reader.pages):
            writer.add_page(reader.pages[page_num])
        else:
            print(f"Warning: {pdf_file} does not have page {page_num + 1}")
# Save the merged PDF
with open(output_pdf, "wb") as out:
    writer.write(out)

print("Merged PDF saved as:", output_pdf)

