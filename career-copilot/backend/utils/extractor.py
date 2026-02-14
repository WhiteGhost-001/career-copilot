import PyPDF2
import io

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Reads a PDF file from bytes and extracts all text.
    """
    try:
        # Load the bytes into a PDF reader object
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
        extracted_text = ""
        
        # Loop through all pages and grab the text
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
                
        # Clean up basic whitespace issues
        cleaned_text = " ".join(extracted_text.split())
        return cleaned_text
        
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        return ""
