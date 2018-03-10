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


# Create a linked list from Array
def LinkedList_From_List(a):
	head = Singly_LinkedList()
	for i in a:
		head.add_to_tail(i)
	return head

# Create a list from LinkedList
def List_from_LinkedList(l):
    out = []
    current = l.head
    while current != None:
        out.append(current.value)
        current = current.next
    return out

# Reverse a Linked List : Iterative Method
def Reverse_LinkedList(l):
    current = l.head
    next_node = None
    previous_node = None
    while current != None:
        next_node = current.next
        current.next = previous_node
        previous_node = current
        current = next_node
        l.head = previous_node
    return l

# Reverse a linked List : Recursive Method
def Reverse_Recursive_LinkedList(l, prev = None):
    current = l
    if not current:
        return prev
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
    return Reverse_Recursive_LinkedList(current, prev)

a = [1, 4, 2, 3, 7, 6, 9, 10]

ll = LinkedList_From_List(a)
rll = Reverse_Recursive_LinkedList(ll.head, prev = None)
print(List_from_LinkedList(rll))
