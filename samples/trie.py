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
      if char not in curr_node.children:
        curr_node.children[char] = Node[char]
      curr_node = curr_node.children[char]

    curr_node.data = string


  def has_data(self, string):
    curr_node = self.head

    for char in string:
      if char in curr_node.children:
        curr_node = curr_node.children[char]
      
      else:
        return False
    
    if curr_node.data != None:
      return True

  def start_with(self, prefix):
    curr_node = self.head
    result = []

    sub_trie = None

    for char in prefix:
      if char in curr_node.children:
        curr_node = curr_node.children[char]
        sub_trie = curr_node
      else:
        return None

    Q = list(sub_trie.children.values())

    while Q:
      curr = Q.pop(0)
      if curr.data != None:
        result.append(curr.data)
      
    Q.extend(list(curr.children.values()))

    return result
