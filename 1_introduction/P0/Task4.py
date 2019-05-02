"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def main():
    calling_numbers = {}
    telephone_marketing_numbers = []

    for item in calls:
        calling_number, _, __, ___ = item;
        calling_numbers[calling_number] = True

    for item in calls:
        _, receiving_number, __, ___ = item;
        if calling_numbers.get(receiving_number):
            calling_numbers[receiving_number] = False

    for item in texts:
        texting_number, receiving_number, __ = item;

        if calling_numbers.get(texting_number):
            calling_numbers[texting_number] = False

        if calling_numbers.get(receiving_number):
            calling_numbers[receiving_number] = False

    for key, value in calling_numbers.items():
        if calling_numbers.get(key):
            telephone_marketing_numbers.append(key)

    print("These numbers could be telemarketers: ")
    print("\n".join(sorted(telephone_marketing_numbers)))

main()
