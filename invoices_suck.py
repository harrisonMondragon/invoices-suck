import sys
import pandas as pd
from pathlib import Path, PurePath

def main():

    sub_files = Path(sys.argv[1]).glob('*')
    create_output_folder(sys.argv[2])

    for file in sub_files:
        sub_df = pd.read_excel(file)
        sub_df.sort_values(by='BILL_DATE')

        # print(sub_df)

def create_output_folder(output: str) -> None:
    if PurePath(output).is_absolute():
        Path.mkdir(output, parents=True, exist_ok=True)
    else:
        Path.mkdir((Path().absolute().joinpath(output)), parents=True, exist_ok=True)

if __name__ == "__main__":
    main()