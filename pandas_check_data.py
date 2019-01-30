import pandas as pd

# CSV directory and filename

csv_dir = 'D:\\Users\\Cormac\\OneDrive\\Family\\Cormac\\College\\NUIG\\Semester 2\\Industrial Development Project\\' \
          'project_starter\\'
file = 'test.csv'

# https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b
missing_values = ["N/A", "N/a", "n/A", "n/a", "Na", "nA","na", "---", "--", "-"]


def read_csv(csv_file):  # Read CSV file
    return pd.read_csv(csv_file, na_values=missing_values)


csv = read_csv(csv_dir + file)

# Gets column labels and then stores as string
h = csv.columns
headers = str(h.tolist())

print(h)
print(headers)
print(csv)


def check_upper(string):  # Check if any letter is upper case print
    if any(i.isupper() for i in string):
        print('Uppercase letter found')


check_upper(headers)


def check_null_values(csv_file):  # Check all values are present and that no rows are too long
    if csv_file.isnull().values.any():
        print('Null value found')


check_null_values(csv)
