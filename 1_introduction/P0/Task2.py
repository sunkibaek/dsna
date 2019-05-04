"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

def main():
    durations = defaultdict(int)
    longest = 0
    longest_number = ""

    for item in calls:
        (calling_number, receiving_number, at_time, duration) = item

        duration = int(duration)

        durations[calling_number] += duration
        durations[receiving_number] += duration

        if durations[calling_number] > longest:
            longest = durations[calling_number]
            longest_number = calling_number

        if durations[receiving_number] > longest:
            longest = durations[receiving_number]
            longest_number = receiving_number

    print(f'{longest_number} spent the longest time, {longest} seconds, on the phone during September 2016.')

main()
