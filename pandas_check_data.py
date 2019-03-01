import load_csv as load
import check_csv as check

# CSV directory and filename
csv_dir = 'D:\\Users\\Cormac\\OneDrive\\Family\\Cormac\\College\\NUIG\\Semester 2\\Industrial Development Project\\' \
          'project_starter\\'
file = 'test2.csv'

csv = load.read_csv(csv_dir + file)
headers = load.get_headers(csv)

print(headers)
print(csv)

check.check_upper(headers)
if check.check_null_values(csv):
    print('Null value found')

print(load.count_records(csv))
check.check_characters(csv, headers)
