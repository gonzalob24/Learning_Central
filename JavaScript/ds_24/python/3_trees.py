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
    
    return tree
  
  def traverse(self):
    return self.traverse_helper(self.root)


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
    
print(find_min([3,1,2]))

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
      found_value = self.search_by_timestamp(values, timestamp)
      if found_value:
          return found_value[0]
      else:
        if values:
          return values[-1][0]
        else:
          return "null"
    
    def search_by_timestamp(self, values, timestamp):
      left = 0
      right = len(values) - 1
      mid = (left + right) // 2

      while left <= right:
        if values[mid][1] == timestamp:
          return values[mid]
        elif values[mid][1] < timestamp:
          left = mid + 1
        else:
          right = mid - 1
        mid = (left + right) // 2
      return False

key = {}

key["one"] = [['foo', 1]]

print(key)
key['one'].append(['bar', 2])
print(key.get('two'))