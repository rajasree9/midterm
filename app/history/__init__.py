import pandas as pd
import logging
import os

class CalculationHistory:
    def __init__(self, csv_file='./data/calculation_history.csv'):
        self.csv_file = csv_file
        self.history_df = self.load_history()

    def load_history(self):
        if os.path.exists(self.csv_file):
            try:
                return pd.read_csv(self.csv_file)
            except Exception as e:
                print(f"Error loading history from CSV: {e}")
                return pd.DataFrame(columns=['Operation', 'Value1', 'Value2'])
        else:
            return pd.DataFrame(columns=['Operation', 'Value1', 'Value2'])

    def save_history(self):
        try:
            self.history_df.to_csv(self.csv_file, index=False)
            print(f"History saved to CSV at '{self.csv_file}'.")
        except Exception as e:
            print(f"Error saving history to CSV: {e}")

    def add_record(self, operation, value1, value2):
        self.history_df = self.load_history()
        new_record = pd.DataFrame({'Operation': [operation], 'Value1': [value1], 'Value2': [value2]})
        self.history_df = pd.concat([self.history_df, new_record], ignore_index=True)
        self.save_history()

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Operation', 'Value1', 'Value2'])
        self.save_history()
        self.history_df = self.load_history()

    def delete_record(self, index):
        try:
            self.history_df.drop(index=index, inplace=True)
            print(f"Record at index {index} deleted from history.")
            self.save_history()
            self.history_df = self.load_history()
        except Exception as e:
            print(f"Error deleting record from history: {e}")
  
