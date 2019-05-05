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
    calling_numbers = set()

    for item in calls:
        calling_number, _, __, ___ = item

        calling_numbers.add(calling_number)

    for item in calls:
        _, receiving_number, __, ___ = item

        calling_numbers.discard(receiving_number)

    for item in texts:
        texting_number, receiving_number, __ = item

        calling_numbers.discard(texting_number)
        calling_numbers.discard(receiving_number)

    print("These numbers could be telemarketers: ")
    print("\n".join(sorted(calling_numbers)))

main()
