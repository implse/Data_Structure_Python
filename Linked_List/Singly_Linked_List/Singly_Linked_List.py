class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

class Singly_LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	# Add value to head of list
	def add_to_head(self, value):
		new_node = Node(value)
		if self.head:
			new_node.next = self.head
			self.head = new_node
		else:
			self.head = new_node
			self.tail = new_node
		self.size += 1

	# Add value to tail of list
	def add_to_tail(self, value):
		new_node = Node(value)
		if self.tail:
			self.tail.next = new_node
			self.tail = new_node
		else:
			self.head = new_node
			self.tail = new_node
		self.size += 1

	# Add value at specific index in list
	def add_at(self, value, index):
		new_node = Node(value)
		previous = None
		current = self.head
		i = 0
		while i < index and current.next:
			previous = current
			current = current.next
			i += 1
		if i == index:
			previous.next = new_node
			new_node.next = current
			return True
		else:
			return False

	# Remove value: return true or false
	def remove(self, value):
		previous = None
		current = self.head
		while current:
			if current.value == value:
				if previous:
					previous.next = current.next
				else:
					self.head = current.next
				self.size -= 1
				return True
			previous = current
			current = current.next
		return False

	# Find if value is in list: return true or false
	def find(self, value):
		current = self.head
		while current:
			if current.value == value:
				return True
			current = current.next
		return False

	# Reverse the link list
	def reverse(self):
		current = self.head
		next = None
		previous = None
		while current:
			next = current.next
			current.next = previous
			previous = current
			current = next
			self.head = previous
		return self.head

	# Create list from linkedList
	def to_list(self):
		l = []
		current = self.head
		while current:
			l.append(current.value)
			current = current.next
		return l
