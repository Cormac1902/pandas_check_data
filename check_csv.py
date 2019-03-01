import re


def check_upper(array):  # Check if any letter is upper case and print
    for word in array:
        for letter in word:
            if letter.isupper():
                print('Uppercase letter found: ' + word + '(Column: ' + str(array.index(word) + 1) + ')')
                break


def check_null_values(csv_file):        # Check all values are present and that no rows are too long
    if csv_file.isnull().values.any():  # Return true if any null values are found
        return True


def check_characters(csv_file, headers):  # Check for special characters
    line_no = column_no = 0

    for line in csv_file.values:
        line_no += 1
        for word in line:
            column_no += 1
            if isinstance(word, str):  # Don't see to need check non-string values as they won't contain special values
                for letter in word:
                    if re.search('[a-zA-ZÀ-ÿ0-9-_<>=]', letter) is None:  # Include accented characters
                        print('Special character found: ' + letter + ' in word ' + word + ' (' +
                              headers[column_no - 1] + ', line ' + str(line_no) + ')')
                        break

        column_no = 0
