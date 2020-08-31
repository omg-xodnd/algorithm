import sys
sys.stdin = open('5670.txt', 'r')

class Node():
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        curr = self.head

        for char in string:
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]

        curr.data = string

    def input_count(self, string):
        count = 1
        curr = self.head.children[string[0]]

        for char in string[1:]:
            if len(curr.children) > 1 or curr.data:
                count += 1
            curr = curr.children[char]

        return count


def get_answer():
    N = int(input())
    string_list = [''] * N
    T = Trie()
    count = 0

    for i in range(N):
        string = input()
        string_list[i] = string
        T.insert(string)

    for string in string_list:
        c = T.input_count(string)
        count += c

    return round(count/N, 2)


while True:
    try:
        answer = get_answer()
        print('%.2f' % answer)

    except EOFError:
        break