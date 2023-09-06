import sys
import pandas as pd
from pathlib import Path

def main():

    sub_folder = Path(sys.argv[1])
    sub_files = sub_folder.glob('*')

    for file in sub_files:
        sub_df = pd.read_excel(file)
        print(sub_df)


if __name__ == "__main__":
    main()