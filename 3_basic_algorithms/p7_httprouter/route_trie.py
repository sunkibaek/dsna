import re
# A RouteTrie will store our routes and their associated handlers


class RouteTrie:
    def __init__(self, root_handler, not_found_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode("")
        self.root.handler = root_handler
        self.not_found_handler = not_found_handler

    def insert(self, split_path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root

        for partial_path in split_path:
            current = current.insert(partial_path)

        current.handler = handler

    def find(self, split_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self.root

        for partial_path in split_path:
            if current.children.get(partial_path, False):
                current = current.children[partial_path]
            else:
                print(self.not_found_handler)

        print(current.handler)

        # A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.


class RouteTrieNode:
    def __init__(self, partial_path):
        # Initialize the node with children as before, plus a handler
        self.partial_path = partial_path
        self.children = {}
        self.handler = None

    def insert(self, partial_path):
        # Insert the node as before
        if not partial_path in self.children:
            new_child = RouteTrieNode(partial_path)
            self.children[partial_path] = new_child

        return self.children[partial_path]


# The Router class will wrap the Trie and handle


class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path_string, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.route_trie.insert(self.split_path(path_string), handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        self.route_trie.find(self.split_path(path))

    def split_path(self, path_string):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        without_tailing_slashes = re.sub("\/*$", "", path_string)

        if without_tailing_slashes == "":
            without_tailing_slashes = "/"

        return path_string.split(without_tailing_slashes)

# Here are some test cases and expected outputs you can use to test your implementation


# create the router and add a route
# remove the 'not found handler' if you did not implement this
router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home"))
print(router.lookup("/home/about"))  # should print 'about handler'
# should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/"))
# should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/me"))

# Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

# More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.
