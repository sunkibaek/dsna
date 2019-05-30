import sys


class Node(object):
    def __init__(self, freq, char):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None


def build_one_group(nodes):
    if len(nodes) <= 1:
        return nodes

    right = nodes.pop()
    left = nodes.pop()

    parent = Node(left.freq + right.freq, None)
    parent.left = left
    parent.right = right

    nodes.append(parent)

    return sorted(nodes, key=lambda node: -node.freq)


def char_to_bin(char, node, binString):
    if not node.left == None:
        return char_to_bin(char, node.left, binString + "0")

    if not node.right == None:
        return char_to_bin(char, node.right, binString + "1")

    return binString if node.char == char else ""


def string_to_bins(data, node):
    result = ""

    for char in data:
        binString = char_to_bin(node, "", char)
        result += binString

    return result


def bin_to_string(data, head, node, string):
    if not (node.char == None):
        return node.char + bin_to_string(data, head, head, "")

    if len(data) == 0:
        return ""

    first_char = data[0]
    data = data[1:]

    if first_char == "0":
        return bin_to_string(data, head, node.left, string)
    else:
        return bin_to_string(data, head, node.right, string)


def char_to_bin(node, binString, char):
    if node == None:
        return ""

    if node.char == char:
        return binString

    left_bin_string = char_to_bin(node.left, binString + "0", char)
    right_bin_string = left_bin_string

    if left_bin_string == "":
        right_bin_string = char_to_bin(node.right, binString + "1", char)

    return right_bin_string


def huffman_encoding(data):
    frequencies = {}
    ordered_chars = []
    ordered_nodes = []

    for char in data:
        frequencies[char] = (frequencies.get(char) or 0) + 1

    ordered_chars = sorted(
        frequencies, key=lambda char: -frequencies.get(char))

    for char in ordered_chars:
        ordered_nodes.append(Node(frequencies.get(char), char))

    while len(ordered_nodes) > 1:
        ordered_nodes = build_one_group(ordered_nodes)

    tree = ordered_nodes[0]

    bin_data = string_to_bins(data, tree)

    return bin_data, tree


def huffman_decoding(data, tree):
    return bin_to_string(data, tree, tree, "")


def test(test_sentence):
    print("The size of the data is: {}".format(
        sys.getsizeof(test_sentence)))
    print("The content of the data is: {}\n".format(test_sentence))

    encoded_data, tree = huffman_encoding(test_sentence)

    print("The size of the encoded data is: {}".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}".format(
        sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))


test("The bird is the word")
# 57
test("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
# 160
test("ab")
# 39
