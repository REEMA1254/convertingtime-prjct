# PYTHON UTILITY FUNCTIONS
## BY-MARYAM ALI_

#Description
This repository contains a collection of Python utility functions. These functions serve different purposes: time conversion, positive number evaluation, and string analysis based on consonant values.

#Functions
convert_to_24_hour: Converts time from a 12-hour format (AM/PM) to a 24-hour format.
two_positive: Determines if exactly two out of three given numbers are positive.
highest_consonant_value: Calculates the highest value of a substring in a given string, based on consonant values.

# Usage
-convert_to_24_hour(hour, minute, period)
-Converts 12-hour time format to 24-hour format.

# Example: Convert 5:30 PM to 24-hour format
print(convert_to_24_hour(5, 30, 'pm'))  # Output: 17:30  

#two_positive(a, b, c)
Checks if exactly two out of three numbers are positive.
# Example: Check if two out of these three numbers are positive
print(two_positive(2, 4, -3))  # Output: True

# highest_consonant_value(s)
Calculates the highest value of consonant substrings.
# Example: Find the highest consonant substring value
print(highest_consonant_value("z"))  # Output: 26

## Setup/Installation Requirements
- Clone the repository to any desired folder in your computer
- Open the cloned folder with vscode.
- Run individual files in your terminal using the command `pytest`
- And you are good to go

## Technologies used
- python
- Terminal


# CONTRIBUTION
KELVIN KIPCHUMBA 

# Author
Maryam Ali



