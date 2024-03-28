import pandas as pd
import os

class CalculationHistory:
    def __init__(self, csv_file='./data/calculation_history.csv'):
        self.csv_file = csv_file
        self.history_df = self.load_history()

    def load_history(self):
        if os.path.exists(self.csv_file):
            return pd.read_csv(self.csv_file)
        else:
            return pd.DataFrame(columns=['Operation', 'Value1', 'Value2'])

    def save_history(self):
        self.history_df.to_csv(self.csv_file, index=False)

    def add_record(self, operation, value1, value2):
        self.history_df = self.history_df.append({'Operation': operation,
                                                  'Value1': value1,
                                                  'Value2': value2
        },
                                                 ignore_index=True)

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Operation', 'Value1', 'Value2'])

    def delete_record(self, index):
        self.history_df.drop(index=index, inplace=True)

