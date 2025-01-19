from process_handler import process_pdfs

if __name__ == "__main__":
    # Define folder paths
    input_folder = "Input_pdfs"
    json_output_folder = "output_jsons"
    image_output_folder = "extracted_images"
    summary_csv_path = "summary/summary_report.csv"

    # Execute the workflow
    process_pdfs(input_folder, json_output_folder, image_output_folder, summary_csv_path)
