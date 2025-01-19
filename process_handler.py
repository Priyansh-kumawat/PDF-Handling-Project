from handlers.pdf_handler import PDFHandler
from handlers.metadata_handler import MetadataHandler
from handlers.text_handler import TextHandler
from handlers.image_handler import ImageHandler
from handlers.data_handler import DataHandler
from handlers.json_handler import JSONHandler
from handlers.summary_handler import SummaryHandler

def process_pdfs(input_folder, json_output_folder, image_output_folder, summary_csv_path):
    """
    Processes all PDFs in the input folder:
    - Extracts metadata, headers, paragraphs, tables, and images.
    - Saves extracted data to JSON files.
    - Saves a summary report to a CSV file.
    """
    # Instantiate handlers
    pdf_handler = PDFHandler(input_folder)
    metadata_handler = MetadataHandler()
    text_handler = TextHandler()
    image_handler = ImageHandler()
    data_handler = DataHandler()
    json_handler = JSONHandler()
    summary_handler = SummaryHandler()

    # Fetch all PDF files
    pdf_files = pdf_handler.get_pdfs()
    summary_data = []  # Initialize summary data list

    for pdf_path in pdf_files:
        print(f"Processing: {pdf_path}")

        # Step 1: Extract metadata
        metadata = metadata_handler.extract_metadata(pdf_path)

        # Step 2: Check if the PDF is empty
        from pypdf import PdfReader
        try:
            reader = PdfReader(pdf_path)
            if len(reader.pages) == 0:
                print(f"Skipping empty PDF: {pdf_path}")
                continue
        except Exception as e:
            print(f"Error reading {pdf_path}: {e}")
            continue

        # Step 3: Extract text, headers, and tables
        headers, paragraphs, tables = text_handler.extract_text_headers_tables(pdf_path)
        cleaned_paragraphs = data_handler.normalize_text(paragraphs)
        dataframes = [data_handler.convert_table_to_dataframe(table) for table in tables if len(table) > 1]

        # Step 4: Extract images
        image_count = image_handler.extract_images(pdf_path, image_output_folder)

        # Step 5: Save extracted data to a JSON file
        json_data = {
            "metadata": metadata,
            "headers": headers,
            "paragraphs": cleaned_paragraphs,
            "tables": [df.to_dict(orient="records") for df in dataframes],
        }
        json_output_path = f"{json_output_folder}/{pdf_path.split('/')[-1].replace('.pdf', '_data.json')}"
        json_handler.save_to_json(json_data, json_output_path)

        # Step 6: Add data to the summary
        summary_data.append({
            "File Name": pdf_path.split("/")[-1],
            "Title": metadata['Title'],
            "Author": metadata['Author'],
            "Pages": metadata['Pages'],
            "Number of Headers": len(headers),
            "Number of Paragraphs": len(cleaned_paragraphs),
            "Number of Tables": len(dataframes),
            "Number of Images": image_count
        })

    # Step 7: Save the summary report to a CSV
    summary_handler.save_summary_to_csv(summary_data, summary_csv_path)
