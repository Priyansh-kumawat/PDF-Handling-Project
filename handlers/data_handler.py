import pandas as pd

class DataHandler:
    def normalize_text(self, paragraphs):
        """
        Cleans and normalizes paragraphs by removing extra spaces and line breaks.
        """
        return [p.strip().replace('\n', ' ') for p in paragraphs if p.strip()]

    def convert_table_to_dataframe(self, table):
        """
        Converts a table (list of lists) into a Pandas DataFrame and ensures unique column names.
        """
        df = pd.DataFrame(table[1:], columns=table[0])
        df.columns = pd.Series(df.columns).apply(lambda x: f"{x}_{list(df.columns).index(x)}" if list(df.columns).count(x) > 1 else x)
        return df
