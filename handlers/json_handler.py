import os
import json

class JSONHandler:
    def save_to_json(self, data, json_output_path):
        """
        Saves extracted data into a JSON file.
        """
        os.makedirs(os.path.dirname(json_output_path), exist_ok=True)
        try:
            with open(json_output_path, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"Saved JSON to {json_output_path}")
        except Exception as e:
            print(f"Error saving JSON: {e}")
