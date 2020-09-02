import sys
sys.stdin = open('5052.txt', 'r')

class Node():

    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie():

    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr_node = self.head

        for char in string:
            if curr_node.data:
                return False

            if char not in curr_node.children:
                curr_node.children[char] = Node(char)
            curr_node = curr_node.children[char]

        curr_node.data = string
        return True

    def is_consistent_with(self, string):
        curr_node = self.head

        for char in string:
            curr_node = curr_node.children[char]

        if curr_node.children:
            return False

        return True


def get_answer(N, string_list):
    T = Trie()

    for string in string_list:
        if not T.insert(string):
            return 'NO'

    for string in string_list:
        if not T.is_consistent_with(string):
            return 'NO'

    return 'YES'


for tc in range(1, int(input())+1):
    N = int(input())
    string_list = [input() for _ in range(N)]
    print(get_answer(N, string_list))