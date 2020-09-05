class Node():
    def __init__(self):
        self.count = 0
        self.child = {}

class Trie():
    def __init__(self):
        self.head = Node(None)

    def insert(self, str):
        curr = self.head

        for c in str:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]
            curr.count += 1

        curr.data = str

    def search(self, query):
        curr = self.head
        q = query.replace("?", "")

        for char in q:
            if char not in curr.child:
                return 0
            curr = curr.child[char]

        return curr.count


def solution(words, queries):
    answer = []

    T = [Trie() for _ in range(10002)]
    T_reverse = [Trie() for _ in range(10002)]

    for word in words:
        T[len(word)].insert(word)

    for word in words:
        word_r = word[::-1]
        T_reverse[len(word)].insert(word_r)

    for query in queries:
        if query[0] == "?":
            answer.append(T_reverse[len(query)].search(query[::-1]))
        else:
            answer.append(T[len(query)].search(query))

    return answer


w = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
q = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(w, q))