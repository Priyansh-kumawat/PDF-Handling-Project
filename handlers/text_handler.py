import pdfplumber

class TextHandler:
    def extract_text_headers_tables(self, pdf_path):
        """
        Extracts headers, paragraphs, and tables from a PDF using font size and formatting.
        """
        headers = []
        paragraphs = []
        tables = []

        try:
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    # Extract full text for paragraphs
                    full_text = page.extract_text()
                    if full_text:
                        lines = full_text.split("\n")
                        para = ""
                        for line in lines:
                            if line.strip():  # If the line is not empty
                                para += line.strip() + " "  # Accumulate text into a paragraph
                            else:
                                if para:  # Add the paragraph if it exists
                                    paragraphs.append(para.strip())
                                    para = ""  # Reset for the next paragraph
                        if para:  # Add the last paragraph if text remains
                            paragraphs.append(para.strip())

                    # Extract words for headers based on font size and boldness
                    for word in page.extract_words():
                        text = word['text']
                        font_size = word.get('size', None)
                        font_name = word.get('fontname', '').lower()  # Get font name (case insensitive)

                        # Identify headers
                        if word['x0'] < 100 and word['x1'] > (page.width - 100):  # Centered text
                            headers.append(text.strip())
                        if font_size and font_size > 12:  # Example threshold for font size
                            headers.append(text.strip())
                        elif "bold" in font_name or "black" in font_name:  # Detect bold fonts
                            headers.append(text.strip())

                    # Extract tables
                    table_data = page.extract_table()
                    if table_data:
                        tables.append(table_data)
        except Exception as e:
            print(f"Error extracting text, headers, and tables from {pdf_path}: {e}")

        return headers, paragraphs, tables
