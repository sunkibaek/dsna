In this problem, an index that devides input into two sections is found first.
After that we determine which section the target value belongs to. And we
binary search the target only inside of the found section.

To determine at where the two sections devide we need to go through all the
elements of the input giving us O(n). After that binary-search runs O(log n).
