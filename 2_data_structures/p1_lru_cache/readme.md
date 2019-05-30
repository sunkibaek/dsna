In this solution I have chosen to use python dictionary to save cache data and
python list to store cache keys.

By using dictionary, cache result can be retrieved at constant time, O(1). Cache
insertion is also at constant time since it is writing to python dictionary.

However, dictionary does not maintain element insertion orders, a separate
double-end queue data structure has been used to decide which cache will be
removed when it reaches its maximum capacity.
