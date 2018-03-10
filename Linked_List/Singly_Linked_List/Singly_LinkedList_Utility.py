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
