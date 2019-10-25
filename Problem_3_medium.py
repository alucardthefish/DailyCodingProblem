"""
Problem 3 (Medium)
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.

For example, given the following Node class
"""


class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def serialize(root):
	"""Transform from obj Node to string"""
	if type(root) is not Node:
		return "[]"
	else:
		leftNode = root.left
		rightNode = root.right
		return "['" + root.val + "', " + serialize(leftNode) + ", " + serialize(rightNode) + "]"


def deserialize(serial_string):
	"""Transform from serial String to object Node"""
	serialList = eval(serial_string)
	return deserial_rec(serialList)


def deserial_rec(list_node):
	if len(list_node) == 0:
		return None
	else:
		node = Node(list_node[0], deserial_rec(list_node[1]), deserial_rec(list_node[2]))
		return node


node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
