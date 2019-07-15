Insert: using the character as a key, save the character node into children dictionary.
Mark the last character as is_word to determine the word.
It takes O(m) with m being the length of a word given.

Find: using the character as a key, find from children and children's children, and so forth.
It takes O(m) with m being the length of a prefix given.

Suffixes: similar to find but recursively add to the result found characters
It takes O(n) since we have to iterate through all the children of all nodes.

(Copied and pasted from the solution made in Jupyter Notebook)
