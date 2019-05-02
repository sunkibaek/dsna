"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def is_bangalore_fixed_line(phone_number):
  matchObj = re.match(r'^(\(080\))(.*)', phone_number)

  if matchObj and matchObj.group(1) == "(080)":
    return True

  return False

def get_prefix(phone_number):
  matchObj = re.match(r'^((140)|([789]\d{4} )|(\(0\d*\)))(\d*)$', phone_number)

  return matchObj.group(1) if matchObj else phone_number

def get_percent(to_number, from_number):
  return round((to_number / from_number) * 100, 2)

def main():
  area_codes = {}
  from_fixed_lines_in_bagalore_count = 0
  to_fixed_lines_in_bangalore_count = 0

  for item in calls:
    calling_number, receiving_number, _, __ = item;

    if not is_bangalore_fixed_line(calling_number):
      continue

    area_codes[get_prefix(receiving_number)] = True
    from_fixed_lines_in_bagalore_count += 1

    if is_bangalore_fixed_line(receiving_number):
      to_fixed_lines_in_bangalore_count += 1

  from_to_bangalore_fixed_lines_percent = get_percent(to_fixed_lines_in_bangalore_count, from_fixed_lines_in_bagalore_count)

  print('The numbers called by people in Bangalore have codes:')
  print("\n".join(sorted(area_codes.keys())))

  print(f'{from_to_bangalore_fixed_lines_percent} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')

main()
