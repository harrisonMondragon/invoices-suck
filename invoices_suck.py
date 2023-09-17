from client import Client
import sys
import pandas as pd
from pathlib import Path, PurePath

def main():
    sub_files = Path(sys.argv[1]).glob('*')
    out_path = create_output_folder(sys.argv[2])

    client_dict = {}

    for file in sub_files:
        sub_df = pd.read_excel(file)
        register_clients(sub_df, out_path, client_dict)
        distribute_entries(sub_df, client_dict, file.stem)

    # TODO: Remove this loop, it just proves the dataframes are correct
    for key in client_dict:
        print(f"DF for key {key}")
        print(client_dict[key].time_df)

def create_output_folder(output: str) -> Path:
    if PurePath(output).is_absolute():
        out = output
    else:
        out = Path().absolute().joinpath(output)

    Path.mkdir(out, parents=True, exist_ok=True)
    return out

def register_clients(df: pd.DataFrame, out: Path, client_dict: dict) -> None:
    for row in df.itertuples():
        client_name = getattr(row, "CLIENT_ID")
        client_path = out.joinpath(client_name)

        # TODO: Change this to depend on the client being in the dict. Want to
        # make dir and re-write it regardless of if it exists or not
        if not client_path.is_dir():
            Path.mkdir(client_path, parents=True, exist_ok=True)
            client_dict[client_name] = Client(client_path, client_name)

def distribute_entries(sub_df: pd.DataFrame, client_dict: dict, sub_name: str) -> None:
    for row in sub_df.itertuples():
        client_name = getattr(row, "CLIENT_ID")
        client_dict[client_name].add_entry(row, sub_name)


if __name__ == "__main__":
    main()