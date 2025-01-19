import os
import pandas as pd

class SummaryHandler:
    def save_summary_to_csv(self, summary_data, summary_csv_path):
        """
        Saves the summary data to a CSV file.
        """
        os.makedirs(os.path.dirname(summary_csv_path), exist_ok=True)
        try:
            df = pd.DataFrame(summary_data, columns=['File Name', 'Title', 'Author', 'Pages', 
                                                     'Number of Headers', 'Number of Paragraphs', 
                                                     'Number of Tables', 'Number of Images'])
            df.to_csv(summary_csv_path, index=False)
            print(f"Summary report saved to {summary_csv_path}")
        except Exception as e:
            print(f"Error saving summary report: {e}")
