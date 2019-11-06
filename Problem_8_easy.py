from Problem_3_medium import Node

# This problem was asked by Google.
#
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#
# Given the root to a binary tree, count the number of unival subtrees.
#
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     /	\
#    1	 0
#   /  \
#  1	1


# Create the example bin tree structure re-using node object from problem 3 (binary tree structure)
root_node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
counter = 0		# Global variable to store number of univals in the tree


def count_univals(root):
	global counter
	counter = 0
	count_univals_rec(root)
	return counter


def count_univals_rec(root):
	global counter
	if not root.left and not root.right:
		counter += 1
	else:
		if is_unival(root):
			counter += 1
		count_univals_rec(root.left)
		count_univals_rec(root.right)
	return counter


def is_unival(root):
	node_val = root.val
	return node_val == root.left.val == root.right.val


# Example
num_univals = count_univals(root_node)
print("Number of univals:", num_univals)
