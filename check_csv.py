import re
import math
import column


def check_upper(array):  # Check if any letter is upper case and print
    for word in array:
        for letter in word:
            if letter.isupper():
                print('Uppercase letter found: ' + word + ' (Column: ' + str(array.index(word) + 1) + ')')
                break


def check_null_values(array):        # Check all values are present and that no rows are too long
    if array.isna().values.any():    # Return true if any null values are found
        return True


def check_null_values_tuples(value):    # Check all values are present and that no rows are too long (for tuples)
    if isinstance(value, float):        # Only floats can be NaN
        if math.isnan(value):           # Return true if any null values are found
            return True
        else:
            return False


def check_characters(value, regex_string):  # Check for special characters
    if isinstance(value, str):  # Don't see need to check non-string values as they won't contain special values
        for letter in value:
            if re.search(regex_string, letter) is None:
                return True


def check_against_array(row, column_obj):   # Check if value exists in array
    value = getattr(row, column_obj.name)   # Get attribute by name of Column object
    if check_value(value) is None:          # No need to check if it's already been dealt with
        if value in column_obj.list:
            return True
        else:
            return value
    else:
        return True


def check_value(value):                                     # Could pass regex here obviously if so desired
    null_value = check_null_values_tuples(value)
    if null_value:
        return 'Null value '
    elif null_value is None:  # check_null_values_tuples returns False if it's a float that isn't NaN
        if check_characters(value, '[a-zA-ZÀ-ÿ0-9-_<>=]'):  # Include accented characters
            return 'Special character '


def print_row_number(row, row_error):  # Prints row number
    if not row_error:                  # Check if row number has been printed
        print(str(row.Index + 2) + ": ")
        row_error = True

    return row_error


def check_against_array_output(row, row_error, column_obj):     # Output for check_against_array
    if isinstance(column_obj, column.Column):                   # Checks if column object has been passed
        chk = check_against_array(row, column_obj)
        if chk is not True:                                     # If check_against_array flags an invalid value
            row_error = print_row_number(row, row_error)
            print('Invalid value found in column ' + column_obj.name + ': ' + chk)

        return row_error


def check_rows(csv_file, headers, column_checks):
    for row in csv_file.itertuples():           # Iterate over rows as named tuples
        row_error = False                       # Variable to ensure row number is only printed once
        for i, value in enumerate(row):         # enumerate for printing out header later
            chk = check_value(value)            # Check value
            if chk is not None:
                row_error = print_row_number(row, row_error)
                print(chk + 'found in column ' + headers[i - 1])

        if isinstance(column_checks, list):     # If list is passed
            for element in column_checks:
                row_error = check_against_array_output(row, row_error, element)
        else:                                   # If list is not passed
            check_against_array_output(row, row_error, column_checks)
