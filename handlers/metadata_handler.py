from pypdf import PdfReader

class MetadataHandler:
    def extract_metadata(self, pdf_path):
        """
        Extracts metadata such as Title, Author, and the number of pages from a PDF.
        """
        try:
            reader = PdfReader(pdf_path)
            metadata = reader.metadata
            return {
                "Title": metadata.get('/Title', 'Unknown'),
                "Author": metadata.get('/Author', 'Unknown'),
                "Pages": len(reader.pages)
            }
        except Exception as e:
            print(f"Error extracting metadata from {pdf_path}: {e}")
            return {"Title": "Unknown", "Author": "Unknown", "Pages": 0}
