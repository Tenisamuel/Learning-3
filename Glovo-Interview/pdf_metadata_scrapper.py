from PyPDF2 import PdfReader

def extract_pdf_metadata(pdf_file):
    reader = PdfReader(pdf_file)
    metadata = reader.metadata

    print("\nPDF Metadata:\n")
    for key, value in metadata.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    file_path = "sample.pdf"  # Replace with your PDF file
    extract_pdf_metadata(file_path)