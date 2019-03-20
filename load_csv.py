import pandas as pd
# import check_csv as check

# https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
missing_values = ["N/A", "N/a", "n/A", "n/a", "Na", "nA","na", "---", "--", "-", " ", "?"]


def read_csv(csv_file):  # Read CSV file
    return pd.read_csv(csv_file, na_values=missing_values)


def get_headers(csv_file):  # Obtain headers from CSV file
    return csv_file.columns.tolist()


def count_records(csv_file):                 # Count records in file
    # if check.check_null_values(csv_file):  # If columns are of unequal lengths, return length of each
    #    return csv_file.count()
    # else:                                  # Otherwise, return length of one column
        return len(csv_file)
