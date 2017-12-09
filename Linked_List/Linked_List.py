class Node(object):
	def __init__(self, value):
		self.value = value
		self.next_node = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	# Add value to head of list
	def add_to_head(self, value):
		new_node = Node(value)
		if self.head:
			new_node.next_node = self.head
			self.head = new_node
		else:
			self.head = new_node
		self.size += 1

	# Add value to tail of list
	def add_to_tail(self, value):
		new_node = Node(value)
		if self.tail:
			self.tail.next_node = new_node
			self.tail = new_node
		else:
			self.head = new_node
			self.tail = new_node
		self.size += 1

	# Add value at specific index in list
	def add_at(self, value, index):
		new_node = Node(value)
		previous_node = None
		current_node = self.head
		i = 0
		while i < index and current_node.next_node:
			previous_node = current_node
			current_node = current_node.next_node
			i += 1
		if i == index:
			previous_node.next_node = new_node
			new_node.next_node = current_node
			return True
		else:
			return False

	# Remove value: return true or false
	def remove(self, value):
		previous_node = None
		current_node = self.head
		while current_node:
			if current_node.value == value:
				if previous_node:
					previous_node.next_node = current_node.next_node
				else:
					self.head = current_node.next_node
				self.size -= 1
				return True
			previous_node = current_node
			current_node = current_node.next_node
		return False

	# Find if value is in list: return true or false
	def find(self, value):
		current_node = self.head
		while current_node:
			if current_node.value == value:
				return True
			current_node = current_node.next_node
		return False

	# Reverse the link list
	def reverse(self):
		current_node = self.head
		next_node = None
		previous_node = None
		while current_node:
			next_node = current_node.next_node
			current_node.next_node = previous_node
			previous_node = current_node
			current_node = next_node
			self.head = previous_node
		return self.head

	# Create list from linkedList
	def to_list(self):
		l = []
		current_node = self.head
		while current_node:
			l.append(current_node.value)
			current_node = current_node.next_node
		return l
