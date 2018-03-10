# Create a Double LinkedList from Array
def DoubleLinkedList_From_List(a):
    head = Node(a[0])
    current = head
    for item in a[1:]:
        new_node = Node(item)
        new_node.prev = current
        current.next = new_node
        current = current.next
    return head

# Create a list from DoubleLinkedList
def List_from_DoubleLinkedList(l):
    out = []
    current = l.head
    while current != None:
        out.append(current.value)
        current = current.next
    return out
