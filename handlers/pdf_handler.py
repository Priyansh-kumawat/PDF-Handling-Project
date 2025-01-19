import os

class PDFHandler:
    def __init__(self, input_folder):
        self.input_folder = input_folder

    def get_pdfs(self):
        """
        Fetches all PDF files from the input folder.
        """
        try:
            pdf_files = [os.path.join(self.input_folder, f) for f in os.listdir(self.input_folder) if f.endswith('.pdf')]
            return pdf_files
        except FileNotFoundError:
            print(f"The directory '{self.input_folder}' does not exist.")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
