import load_csv as load
import check_csv as check
import os

# CSV directory and filename
csv_dir = 'D:\\Users\\Cormac\\OneDrive\\Family\\Cormac\\College\\NUIG\\Semester 2\\Industrial Development Project\\' \
          'project_starter'
file = 'test2.csv'

csv = load.read_csv(os.path.join(csv_dir, file))
headers = load.get_headers(csv)

print(headers)
print(csv)

check.check_upper(headers)
# if check.check_null_values(csv):
#     print('Null value found')

# To show can be used on record as well as file
# if check.check_null_values(csv.iloc[4]):
#     print('Null value found')

print(load.count_records(csv))
for row in csv.itertuples():                    # Iterate over rows as named tuples
    row_error = False                           # Variable to ensure row number is only printed once
    for i, value in enumerate(row):             # enumerate for printing out header later
        chk = check.check_value(value)          # Check value
        if chk is not None:
            if not row_error:                   # Check if row number has been printed
                print(str(row.Index + 1) + ": ")
                row_error = True                # Set row_error to True
            print(chk + 'found in column ' + headers[i - 1])
