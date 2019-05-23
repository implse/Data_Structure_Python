class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]
    # Hash Function
    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    # Set key, value
    def set(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # Collision
        number_collisions = 1

        while(current_array_value[0] != key):
          new_hash_code = self.hash(key, number_collisions)
          new_array_index = self.compressor(new_hash_code)
          current_array_value = self.array[new_array_index]

          if current_array_value is None:
              self.array[new_array_index] = [key, value]
              return

          if current_array_value[0] == key:
              self.array[new_array_index] = [key, value]
              return

          number_collisions += 1

        return

    # Get value from Key
    def get(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        while (possible_return_value != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

        return

    # Return the Keys
    def keys(self):
            for k in self.array:
                if k != None:
                    print(k[0])
    # Return Key Value
    def items(self):
        for k in self.array:
            if k != None:
                print((k[0], k[1]))





# Test

hash_map = HashMap(20)
hash_map.set("John Coltrane", "North Carolina")
hash_map.set("Charlie Parker", "Missouri")
hash_map.set("Charles Mingus", "Arizona")
hash_map.set("Duke Ellington", "Ohio")
hash_map.set("Dizzy Gillepsie", "South Carolina")
hash_map.set("Thelonious Monk", "South Carolina")
hash_map.set("Bill Evans", "New Jersey")


print(hash_map.get("John Coltrane"))

hash_map.keys()
hash_map.items()
