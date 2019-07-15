add_handler: To add handler we go through partial path of each splitted path and
insert partial_path. When we reach the end we add the handler. It takes O(m) with m
being the length of splitted path.

lookup: To look up a route we go through the partial path of each splitted path and
see if children has the route. It takes O(m) with m being the length of splitted path.

split_path: This method has been used to split path into partial paths. It uses
regex matching and python's built in string split method. It might add extra
O(m) time to each operation with m being the length of path_string.

(Copied and pasted from the solution made in Jupyter Notebook)
