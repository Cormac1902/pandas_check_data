import re


def check_upper(array):  # Check if any letter is upper case and print
    for word in array:
        for letter in word:
            if letter.isupper():
                print('Uppercase letter found: ' + word + ' (Column: ' + str(array.index(word) + 1) + ')')
                break


def check_null_values(array):        # Check all values are present and that no rows are too long
    if array.isnull().values.any():  # Return true if any null values are found
        return True


def check_characters(csv_file, headers, regex_string):  # Check for special characters
    for row in csv_file.itertuples():                   # Iterate over rows as named tuples
        for i, word in enumerate(row):                  # enumerate for printing out header later
            if isinstance(word, str):  # Don't see need to check non-string values as they won't contain special values
                for letter in word:
                    if re.search(regex_string, letter) is None:  # Include accented characters
                        print('Special character found: ' + letter + ' in word ' + word + ' (' + headers[i - 1] +
                              ', line ' + str(row.Index + 1) + ')')
                        break
