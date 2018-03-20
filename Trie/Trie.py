class Node(object):
    def __init__(self):
        self.childrens = {}
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.childrens:
                current.childrens[char] = Node()
            current = current.childrens[char]
        current.endOfWord = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.childrens:
                return False
            current = current.childrens[char]
        return current.endOfWord

    def print_words(self):
        list_words = []
        current = self.root
        def lookup(current, word):
            if len(current.childrens) > 0:
                for char in current.childrens:
                    lookup(current.childrens[char], word+char)
                if current.endOfWord:
                    list_words.append(word)
            else:
                if len(word) > 0:
                    list_words.append(word)
                return
        word = ""
        lookup(current, word)
        return list_words if len(list_words) > 0 else None

# Test
trie_test = Trie()
trie_test.insert('mimi')
trie_test.insert('keanu')
trie_test.insert('caramel')
print(trie_test.search('mimi'))
print(trie_test.search('mimigentil'))
print(trie_test.print_words())
