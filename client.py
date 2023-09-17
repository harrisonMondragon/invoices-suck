import pandas as pd
from pathlib import Path

# Needs to be in the correct order for the output
column_names = ["BILL_DATE", "SUB_ID", "PROJECT_ID", "TASK_ID", "HOURS", "DESCR"]

class Client:
    def __init__(self, outpath: Path, client_name: str) -> None:
        # print(f"constructor call for {self.client_name}")
        self.outpath = outpath
        self.client_name = client_name
        self.time_df = pd.DataFrame(columns=column_names)

    def add_entry(self, sub_row: tuple, sub_id: str) -> None:
        # print(f"add_entry call for {self.client_name}")
        row_dict = {}
        for column in column_names:
            if column == "SUB_ID":
                row_dict[column] = sub_id
            else:
                row_dict[column] = getattr(sub_row, column)

        # TODO: Investigate using loc/iloc here, might be faster
        # self.time_df.loc[len(self.time_df)] = row_dict ???
        self.time_df = pd.concat([self.time_df, pd.DataFrame([row_dict])], ignore_index=True)


    def publish(self):
        # print(f"publish call for {self.client_name}")
        """
        Order by date
        time_df.sort_values(by='BILL_DATE')
        Write csv
        """

