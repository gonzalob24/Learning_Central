class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BST:
  
  def __init__(self):
    self.root = None
    
  def insert(self, value):
    new_node = Node(value)
    # edge case: root is None
    if self.root == None:
      self.root = new_node
      return self.root
    
    current_node = self.root
    
    while True:
      if (current_node.value > value):
        if not current_node.left:
          current_node.left = new_node
          return self.root
        else:
          current_node = current_node.left
      else:
        if not current_node.right:
          current_node.right = new_node
          return self.root
        else:
          current_node = current_node.right
  
  def lookup(self, value):
    current_node = self.root
    
    if current_node == None:
      return None
    
    while current_node:
      if current_node.value == value:
        return current_node
      elif current_node.value < value:
        current_node = current_node.right
      else:
        current_node = current_node.left
    return None

  def find_recursion(self, target):
    return self.find_recursion_helper(self.root, target)
  
  def find_recursion_helper(self, node, target):

    if not node:
      return None
    if node.value == target:
      return node.value
    return self.find_recursion_helper(node.left, target) or self.find_recursion_helper(node.right, target)
    
  
  def remove(self):
    pass
  
  def traverse_helper(self, node):
          
    tree = {'value': node.value}

    if node.left == None:
      tree['left'] = None
    else:
      tree['left'] = self.traverse_helper(node.left)
    
    if node.right == None:
      tree['right'] = None
    else: 
      tree['right'] = self.traverse_helper(node.right)
    
    print('Tree Traverse --- ', tree)
    return tree
  
  def traverse(self):
    return self.traverse_helper(self.root)

  def in_order_traversal_helper(self, node):
    if not node:
      return None
    
    # Swap the children
    temp = node.left
    node.left = node.right
    node.right = temp
    
    self.in_order_traversal_helper(node.left)
    self.in_order_traversal_helper(node.right)
    return node
  
  def invert_tree_use_in_order_dfs(self):
    return self.in_order_traversal_helper(self.root)
  
  def tree_depth_dfs(self):
    return self.tree_depth_helper(self.root)
  
  def tree_depth_helper(self, node):
    
    if not node:
      return 0
    left = 1 + self.tree_depth_helper(node.left)
    right = 1 + self.tree_depth_helper(node.right)
    return max(left, right)
  
  def diameter_of_bt(self):
    self.res = 0
    self.diameter_of_bst_helper(self.root)
    return self.res
  
  def diameter_of_bst_helper(self, node):
    
    if not node:
      return 0

    left = self.diameter_of_bst_helper(node.left)
    right = self.diameter_of_bst_helper(node.right)
    self.res = max(self.res, left + right)
    print(self.res)
    return 1 + max(left, right)

bst1 = BST()
bst1.insert(9)
bst1.insert(4);
bst1.insert(20);
bst1.insert(1);
bst1.insert(6);
bst1.insert(8);
bst1.insert(10);
bst1.insert(15);
bst1.insert(170);
print(bst1.traverse())
print(bst1.lookup(11))
print(bst1.lookup(1))

def search(nums, target):
  left = 0
  right = len(nums) - 1
  mid = left + ((right - left) // 2) 
  while left <= right:
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      left = mid + 1
    else: 
      right = mid - 1
    mid = left + ((right - left) // 2) 
  return -1
    
print(search([-1,0,3,5,9,12], 9))

print('Search a 2 D Matrix')

def search_2d_matrix(matrix, target) -> bool:
  
  # Edge cases..
  
  left = 0
  right = len(matrix) - 1
  mid =  left + ((right - left) // 2)
  while left <= right:
    if matrix[mid][0] <= target and target <= matrix[mid][-1]:
      # search for item
      inner_left = 0
      inner_right = len(matrix[mid]) - 1
      inner_mid = inner_left + ((inner_right - inner_left) // 2)
      # print(matrix[mid])
      while inner_left <= inner_right:
        if matrix[mid][inner_mid] == target:
          return True
        elif target > matrix[mid][inner_mid]:
          inner_left = inner_mid + 1
        else:
          inner_right = inner_mid - 1
        inner_mid = inner_left + ((inner_right - inner_left) // 2)
        if inner_left > inner_right:
          return False
    elif target < matrix[mid][0]:
      right = mid - 1
    elif target > matrix[mid][-1]:
      left = mid + 1
    mid =  left + ((right - left) // 2)
  return False

print(search_2d_matrix([[1,3,5]], 1))

print('Eating Bananas')

import math
def min_eating_speed(piles, h):
  left = 1
  right = max(piles)
  result = right
  
  while left <= right:
    k_mid = (left + right) // 2
    
    total_time = 0
    for pile in piles:
      total_time += math.ceil(float(pile) / k_mid)
      print(left, right, pile, k_mid, total_time)
    if total_time <= h:
      result = k_mid
      right = k_mid - 1
    else:
      left = k_mid + 1
  return result
        
  

print(min_eating_speed([3,6,7,11], 8))

print("Find min in rotated array")

def find_min(nums):
  
  left = 0
  right = len(nums) - 1
  mid = (right + left) // 2
  min_value = nums[0]
  while left <= right:
    print(left, mid, right, left == mid)
    if nums[left] < nums[right]:
      min_value = min(min_value, nums[left])
      break
    if nums[mid] >= nums[right]:
      left = mid + 1
    elif nums[mid] < nums[right]:
      right = mid - 1
    min_value = min(min_value, nums[mid])
    mid = (right + left) // 2
  return min_value
    
print(find_min([5,1,2,3,4]))

print('Search in rotated sorted array')

def search_rotated_array(nums, target):
  
  left = 0
  right = len(nums) - 1
  mid = (right + left) // 2
  
  while left <= right:
    print(left, right, mid)
    if nums[mid] == target:
      return mid
    
    if nums[left] <= nums[mid]:
      if target > nums[mid] or target < nums[left]:
        left = mid + 1
      else:
        right = mid - 1
    else:
      if target < nums[mid] or target > nums[right]:
        right = mid - 1
      else:
        left = mid + 1
  
    mid = (right + left) // 2
  
  return -1

print(search_rotated_array([3,5,1], 3))

class TimeMap:

    def __init__(self):
      
      self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
      if self.key_store.get(key) == None:
          self.key_store[key] = [[value, timestamp]]
      else:
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
      values = self.key_store[key]
      return self.search_by_timestamp(values, timestamp)
      
    
    def search_by_timestamp(self, values, timestamp):
      left = 0
      right = len(values) - 1
      mid = (left + right) // 2
      result = ""
      while left <= right:
        if values[mid][1] <= timestamp:
          result = values[mid][0]
          left = mid + 1
        else:
          right = mid - 1
        mid = (left + right) // 2
      return result

key = {}

key["one"] = [['foo', 1]]

print(key)
key['one'].append(['bar', 2])
print(key.get('two'))

print("Trees")

bst2 = BST()
bst2.insert(4)
bst2.insert(2)
bst2.insert(7)
bst2.insert(1)
bst2.insert(3)
bst2.insert(6)
bst2.insert(9)
print(bst2.traverse())
# bst2.invert_tree_use_in_order_dfs()
print(bst2.traverse())
print('Max Depth')
print(bst2.tree_depth_dfs())

print('Diameter of the tree')
bst3 = BST()
bst3.insert(1)
bst3.insert(2)
bst3.insert(3)
bst3.insert(4)
bst3.insert(5)
print('Traverse BST1 -- ', bst1.traverse())
# print('BST2 -- ', bst2.traverse())
# print('BST3 depth -- ', bst1.tree_depth_dfs())
print("Diameter -- ", bst1.diameter_of_bt())
# print("BST1 - ", bst1.traverse())
# print('Find Recursion -- ', bst1.find_recursion(10))