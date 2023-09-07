import sys
import pandas as pd
from pathlib import Path, PurePath

def main():
    sub_files = Path(sys.argv[1]).glob('*')
    out_path = create_output_folder(sys.argv[2])

    for file in sub_files:
        sub_df = pd.read_excel(file)
        sub_df.sort_values(by='BILL_DATE')
        make_directories(sub_df, out_path)

def create_output_folder(output: str) -> Path:
    if PurePath(output).is_absolute():
        out = output
    else:
        out = Path().absolute().joinpath(output)

    Path.mkdir(out, parents=True, exist_ok=True)
    return out

def make_directories(df: pd.DataFrame, out: Path) -> None:
    for row in df.itertuples():
        client_path = out.joinpath(getattr(row, "CLIENT_ID"))
        if not client_path.is_dir():
            Path.mkdir(client_path, parents=True, exist_ok=True)



if __name__ == "__main__":
    main()