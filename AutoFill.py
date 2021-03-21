class Node:
    def __init__(self, char):
        self.char = char
        self.possible_word = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head
        for char in string:
            curr_node.possible_word += 1
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]
        curr_node.possible_word += 1

    def search(self, string):
        curr_node = self.head
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if curr_node.possible_word == 1:
            return True
        else:
            return False


def solution(words):
    cnt = 0
    word_trie = Trie()
    for word in words:
        word_trie.insert(word)

    for word in words:
        already_find = False

        for i in range(1, len(word)+1):
            if word_trie.search(word[:i]):
                cnt += len(word[:i])
                already_find = True
                break
        if not already_find:
            cnt += len(word)

    return cnt


words = ["go","gone","guild"]
print(solution(words))



















