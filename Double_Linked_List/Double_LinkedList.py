class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None
		self.prev = None

class Double_LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	# Add value to head of list
	def add_to_head(self, value):
		new_node = Node(value)
		if self.head:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node
		else:
			self.head = new_node
		self.size += 1
	# Add value to the tail of List
	def add_to_tail(self, value):
		new_node = Node(value)
		if self.tail:
			self.tail.next = new_node
			new_node.prev = self.tail
			self.tail = new_node
		else:
			self.tail = new_node
			self.head = new_node
