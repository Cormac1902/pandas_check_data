import re
import math


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
    # for i, value in enumerate(array): # enumerate for printing out header later
    if isinstance(value, float):        # Only floats can be NaN
        if math.isnan(value):           # Return true if any null values are found
            return True
            # print('Missing value found in column ' + headers[i - 1] + ', line ' + str(array.Index + 1) + ')')


def check_characters(value, regex_string):                  # Check for special characters
    # for i, word in enumerate(array):                      # enumerate for printing out header later
    if isinstance(value, str):  # Don't see need to check non-string values as they won't contain special values
        for letter in value:
            if re.search(regex_string, letter) is None:
                return True
                # print('Special character found: ' + letter + ' in word ' + word + ' (' + headers[i - 1] +
                #       ', line ' + str(array.Index + 1) + ')')
                # break


def check_value(value):                                 # Could pass regex here obviously if so desired
    if check_null_values_tuples(value):
        return 'Null value '

    if check_characters(value, '[a-zA-ZÀ-ÿ0-9-_<>=]'):  # Include accented characters
        return 'Special character '
