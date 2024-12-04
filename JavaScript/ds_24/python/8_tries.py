class TrieNode:
  
  def __init__(self):
    self.children = {}
    self.is_end_of_word = False
  
  
class Trie:
  
  def __init__(self):
    self.root = TrieNode()
  
  def insert(self, word: str) -> None:
    node = self.root
    
    for char in word:
      if not node.children.get(char):
        node.children[char] = TrieNode()
      
      node = node.children[char]
    
    node.is_end_of_word = True
        

  def search(self, word: str) -> bool:
    node = self.root
    for char in word:
      if not node.children.get(char):
        return False
      node = node.children[char]
    
    return node.is_end_of_word

  def startsWith(self, prefix: str) -> bool:
    node = self.root
    
    for char in prefix:
      if not node.children.get(char):
        return False
      
      node = node.children[char]
    
    return True
  
  def traverse(self):
    node = self.root


t = Trie()
t.view()
t.insert('maria')
t.insert('cat')
t.insert('can')
t.insert('bat')
t.view()