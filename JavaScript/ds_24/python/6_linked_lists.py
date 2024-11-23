class Node:
  
  def __init__(self, value):
    self.value = value
    self.next = None
  
  
class SinglyLL:
  
  def __init__(self):
    self.head = None
    self.tail = None
    
  def reverse_list(self):
    current_node = self.head
    prev = None
    
    while current_node:
      next_node = current_node.next
      current_node.next = prev
      prev = current_node
      current_node = next_node
    self.head = prev  
    return self
  

def merge_two_sorted_lists(list1, list2):
  
  pass


def reorder_list(head):
  
  values = []
  
  while head:
    values.append(head.val)
    head.next
  print(values)

    
    
for i in range(1,len('ddddd'),1):
  print(i)


s = set()
s.add('one')
s.add('two')

print(len(s))
print("1".lower())
s.remove('two')
print(s)