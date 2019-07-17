To achieve the maximum sum, we need to put higher number to the left of each
number. To do so, we sort the input then alternatively assign values to each
number.

Python's built in sorted takes O(n log n) in time and O(n) in space to run.
After that, looping through the sorted list takes O(n) in time and O(1) in space.
