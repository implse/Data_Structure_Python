class Node(object):
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.endOfWord = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.endOfWord

    def print_words(self):
        list_words = []
        current = self.root
        def lookup(current, word):
            if len(current.children) > 0:
                for char in current.children:
                    lookup(current.children[char], word+char)
                if current.endOfWord:
                    list_words.append(word)
            else:
                if len(word) > 0:
                    list_words.append(word)
                return
        word = ""
        lookup(current, word)
        return list_words if len(list_words) > 0 else None
