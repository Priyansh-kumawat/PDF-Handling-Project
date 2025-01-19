import os
import fitz

class ImageHandler:
    def extract_images(self, pdf_path, image_output_folder):
        """
        Extracts images from a PDF and saves them in a subfolder specific to the PDF.
        """
        pdf_name = os.path.basename(pdf_path).replace('.pdf', '')
        pdf_image_output_folder = os.path.join(image_output_folder, pdf_name)
        os.makedirs(pdf_image_output_folder, exist_ok=True)

        image_count = 0
        try:
            with fitz.open(pdf_path) as pdf_document:
                for page_number in range(len(pdf_document)):
                    page = pdf_document[page_number]
                    images = page.get_images(full=True)

                    for img_index, img in enumerate(images):
                        xref = img[0]
                        base_image = pdf_document.extract_image(xref)
                        img_bytes = base_image["image"]
                        img_ext = base_image["ext"]

                        image_path = os.path.join(
                            pdf_image_output_folder,
                            f"page_{page_number + 1}_img_{img_index + 1}.{img_ext}"
                        )
                        with open(image_path, "wb") as f:
                            f.write(img_bytes)
                        image_count += 1
                        print(f"Saved image to {image_path}")
        except Exception as e:
            print(f"Error extracting images from {pdf_path}: {e}")

        return image_count
