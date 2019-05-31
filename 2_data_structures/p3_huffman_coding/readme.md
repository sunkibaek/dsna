In this problem, three parts were significant:

1. building the tree and encoding

Using a sorted array of nodes, started from the nodes with least value so that
they get assigned the biggest binary, and the most frequently used values
assigned smallest binary.

Have to take multiple linear iteration of the list to build the tree so it takes
O(n) time for this task. It also uses python's built-in sorted function which
might take O(n log n).

2. traversing the tree to decode

Used a recursive function with 1 or 0 as a guide to decide whether to go to
a left or right node.

It takes linear time to go through each character of binary and traverse the
tree to find the value.
