Insert: using the character as a key, save the character node into children dictionary.
Mark the last character as is_word to determine the word.
It takes O(m) in time and O(m) in space, with m being the length of a word given.

Find: using the character as a key, find from children and children's children, and so forth.
It takes O(m) in time and O(1) in space, with m being the length of a prefix given.

Suffixes: similar to find but recursively add to the result found characters
It takes O(n) in time since we have to iterate through all the children of all nodes.
It takes O(n \* m) in space with n being all the children nodes and m being the length
of suffixes in children since we have to buidl up a list of suffxies to return.

(Copied and pasted from the solution made in Jupyter Notebook)
