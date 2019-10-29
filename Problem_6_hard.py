import uuid

'''
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and
dereference_pointer functions that converts between nodes and memory addresses.
'''


class XORNode(object):
	def __init__(self, prev, element, nex, index):
		self.element = element
		self.both = prev ^ nex
		self.index = index

	def next_node(self, current_idx):
		return self.both ^ current_idx


class XORLinkListed(object):
	def __init__(self):
		self.collection = {}
		self.HEAD = uuid.uuid4().int  # Set the head unique identifier (initialize)
		self.counter = -1

	def add(self, element):
		self.counter += 1
		if self.counter == 0:
			node = XORNode(-1, element, -1, self.counter)
			self.collection[self.HEAD] = node
		else:
			prev_idx = -1
			current_idx = self.HEAD
			current_node = self.collection[current_idx]
			next_idx = current_node.next_node(prev_idx)

			while next_idx != -1:
				prev_idx, current_idx = current_idx, next_idx
				current_node = self.collection[next_idx]
				next_idx = current_node.next_node(prev_idx)

			new_idx = uuid.uuid4().int  # New identifier
			current_node.both = prev_idx ^ new_idx
			self.collection[new_idx] = XORNode(current_idx, element, -1, self.counter)

	def get(self, idx):
		if 0 <= idx < len(self.collection):
			prev_idx, current_idx = -1, self.HEAD
			current_node = self.collection[current_idx]
			node_index = current_node.index
			while node_index != idx:
				next_idx = current_node.next_node(prev_idx)
				current_node = self.collection.get(next_idx)
				node_index = current_node.index
				prev_idx = current_idx
				current_idx = next_idx
			return current_node.element
		else:
			return "Out of bounds!"
