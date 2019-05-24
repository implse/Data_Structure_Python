from Linked_List import LinkedList, Node

# Hash Map - Seperate Chaining (Linked List)
class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for _ in range(self.array_size)]

    # Hash Function
    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    # Set Key / Value
    def set(self, key, value):
        array_index = self.compress(self.hash(key))
        node = Node([key, value])
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if item[0] == key:
                item[1] = value
                return
        list_at_array.insert(node)

    # Get Value from Key
    def get(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if item[0] == key:
                return item[1]
        return None

    # List all the Keys
    def keys(self):
        for k in self.array:
            current_node = k.head_node
            if current_node != None:
                while current_node:
                    key = current_node.value[0]
                    print(key)
                    current_node = current_node.get_next_node()

    # Return Key-Value Pair
    def items(self):
        for k in self.array:
            current_node = k.head_node
            if current_node != None:
                while current_node:
                    key, value = current_node.value
                    print((key, value))
                    current_node = current_node.get_next_node()
