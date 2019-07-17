To sort numbers in one traversal, we can fill up the result array from left for 0
and from right for 2. For 1s, we can remember the number of 0s and use that
information to store 1s after 0s. We have to iterate the whole list which takes
O(n) in time and each operation for item takes O(1) in time. Since we are essentially
building a copy of sorted list it takes O(n) in space.
