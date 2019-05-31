The challenging part of this problem is to extract common or union elements
from each list. To accomplish that, elements from each list have been pulled
into a set then used to re-create a new list.

For union, we first iterate through the one of the given linked list (O(n)) and
then iterate through the other list (O(n)) and lastly iterate through the list
of common values (O(n)). Putting all together it takes 3xO(n) or O(n) simply.

Intersection is similar but it only iterates two lists so 2xO(n) or O(n) simply.
