import pandas as pd


def get_kdd99_dataset() -> pd.DataFrame:
    """
    Downloads and returns the KDD Cup 1999 dataset with feature names.

    Returns:
        pd.DataFrame: The KDD Cup 1999 dataset as a Pandas dataframe.
    """
    # URL for the dataset with the full 10% version of KDD Cup 1999
    url: str = "http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz"

    # Feature names for the dataset
    column_names: list[str] = [
        "duration",
        "protocol_type",
        "service",
        "flag",
        "src_bytes",
        "dst_bytes",
        "land",
        "wrong_fragment",
        "urgent",
        "hot",
        "num_failed_logins",
        "logged_in",
        "num_compromised",
        "root_shell",
        "su_attempted",
        "num_root",
        "num_file_creations",
        "num_shells",
        "num_access_files",
        "num_outbound_cmds",
        "is_host_login",
        "is_guest_login",
        "count",
        "srv_count",
        "serror_rate",
        "srv_serror_rate",
        "rerror_rate",
        "srv_rerror_rate",
        "same_srv_rate",
        "diff_srv_rate",
        "srv_diff_host_rate",
        "dst_host_count",
        "dst_host_srv_count",
        "dst_host_same_srv_rate",
        "dst_host_diff_srv_rate",
        "dst_host_same_src_port_rate",
        "dst_host_srv_diff_host_rate",
        "dst_host_serror_rate",
        "dst_host_srv_serror_rate",
        "dst_host_rerror_rate",
        "dst_host_srv_rerror_rate",
        "label",
    ]

    # Downloading and loading the dataset
    df: pd.DataFrame = pd.read_csv(url, names=column_names, header=None)

    return df


# Display the first few rows to verify
kdd99_cup_df = get_kdd99_dataset()

kdd99_cup_df.to_csv("kdd-cup-1999-data.csv")
