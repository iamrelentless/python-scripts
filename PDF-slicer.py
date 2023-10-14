import PyPDF2

def extract_pages_from_pdf(input_file, output_file, start_page, end_page):
    with open(input_file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        # Create a new PDF writer
        pdf_writer = PyPDF2.PdfFileWriter()

        # Check if input page range is valid
        if start_page < 1 or end_page > pdf_reader.numPages:
            print("Invalid page range.")
            return
        
        # Extract pages and add to the writer
        for page in range(start_page - 1, end_page): # -1 because pages are 0-indexed
            pdf_writer.addPage(pdf_reader.getPage(page))
        
        # Save to output file
        with open(output_file, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        print(f"Pages {start_page}-{end_page} saved to {output_file}")


# Example Usage:
input_file_path = "path_to_input.pdf"
output_file_path = "path_to_output.pdf"
extract_pages_from_pdf(input_file_path, output_file_path, 45, 60)
