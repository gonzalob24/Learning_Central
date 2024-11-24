from typing import List
import math

print('Contains Duplicates')

def contains_duplicates(nums):
  if len(nums) == 0:
    return False

  unique_keys = {}
  for i in range(len(nums)):
    print(unique_keys)
    print(i, nums[i], nums[i] in unique_keys)
    if not unique_keys.get(str(nums[i])):
      unique_keys[str(nums[i])] = i
    else:
      print('Yes')
      print(unique_keys)
      return True
  print('--', not unique_keys.get('1'))
  return False

print(contains_duplicates([1,2,3,1]))

class Solution:

  def product_except_self(self, nums: List[int]) -> List[int]:
    if len(nums) == 0:
      return []
    results = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
      print(i)
      results[i] = prefix
      prefix *= nums[i]
    print(results)
    postfix = 1
    for i in range(len(nums) -1, -1, -1):
      print(i)
      results[i] *= postfix
      postfix *= nums[i]
    # if len(nums) == 0:
    #   return []
    # results = []
    # cache = {}
    # for i in range(len(nums)):
    #   current_sum = 1
    #   for j in range(len(nums)):
    #     if i != j:
    #       prod = current_sum * nums[j]
    #       current_sum = prod
    #   results.append(current_sum)
    return results
      
print('Product Except Self')
test = Solution()
print(test.product_except_self(nums=[1,2,3,4]))

print(test.product_except_self(nums=[-1,1,0,-3,3]))

# for i in range(4-1, -1, -1):
#   print(i)

def longest_consecutive_sequence(nums):
  # calling sorted is nlogn
  # return sorted(nums)
  nums_set = set(nums)
  max_consecutive_sequence = 0
  # for num in nums:
  #   counter = 0
  #   next_value = num
  #   while (next_value in nums_set):
  #     counter += 1
  #     max_consecutive_sequence = max(max_consecutive_sequence, counter)
  #     next_value += 1
  
  for num in nums:
    # check to see if it has a left neighbor. Recognize patterns, draw on number line if needed
    if (num - 1) not in nums_set:
      counter = 1
      while (num + counter) in nums_set:
        counter += 1
      max_consecutive_sequence = max(max_consecutive_sequence, counter)
  
  return max_consecutive_sequence
  


print(longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]))

def is_valid_parentheses(s) -> bool:
  stack = []
  parentheses_hash = {")":"(", "]":"[", "}":"{"}
  if len(s) == 1:
    return False
  
  for char in s:
    # print(parentheses_hash[char])
    if parentheses_hash.get(char) and len(stack) == 0:
      return False
    elif parentheses_hash.get(char) and len(stack) != 0:
      popped_item = stack.pop()
      if parentheses_hash[char] != popped_item:
        return False
    else:
      stack.append(char)
  return True
  

s = set([100,3,7,2,5,8,4,6,0,1])
# for ch in "hello":
#   print(ch)

print(is_valid_parentheses("}}"))

print('Min Stack')
class MinStack:

  def __init__(self):
    self.min = []
    self.stack = []
    
  def push(self, val: int) -> None:
    if len(self.min) == 0:
      self.min.append(val)
    else:
      new_min = min(self.min[-1], val)
      self.min.append(new_min)
    self.stack.append(val)

  def pop(self) -> None:
    self.min.pop()
    return self.stack.pop()
  
  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.min[-1]

minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.push(-6)
print(minStack.getMin()); 
print(minStack.pop());
print(minStack.top());   
print(minStack.getMin());
print("Evaluate RPN")

import operator
def evalRPN(tokens):
  valid_operators = dict({"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv})
  stack = []
  for token in tokens:
    if token not in valid_operators:
      stack.append(int(token))
    else:
      top = stack.pop()
      next = stack.pop()
      if token == "/":
        result = math.trunc(next/top)
      else:
        result = valid_operators[token](next, top)
      stack.append(int(result))
  return stack.pop()

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

print("Daily temps")

def daily_temps(temps):
  temp_stack = []
  days_till_next_warmer_temp = [0] * len(temps)
  
  for i, temp in enumerate(temps):
    while temp_stack and temp_stack[-1][1] < temp:
      index, popped_temp = temp_stack.pop()
      days_till_next_warmer_temp[index] = i - index
    temp_stack.append((i, temp))
  
  return days_till_next_warmer_temp

# for day, temp in enumerate([73,74,75,71,69,72,76,73]):
#   print(day, temp)

# s = [0] * 10
# print(s)

print(daily_temps([73,74,75,71,69,72,76,73]))

print("Car Fleet")
def car_fleet(target, positions, speeds):
  pos_speed_pair = list(zip(positions, speeds))
  pos_speed_pair.sort(reverse=True)
  stack = []
  fleet = 0
  # for p, s in pos_speed_pair:
  #   time = (target - p) / s
  #   while stack and stack[-1] <= time:
  #     stack.pop()
  #     fleet += 1
  #   stack.append(time)
  for pos, sp in pos_speed_pair:
    time = (target - pos) / sp
    stack.append(time)
    if len(stack) >= 2 and stack[-1] <= stack[-2]:
      stack.pop()
  
  
  return len(stack)

print(car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]))

# el = list(zip([10,8,0,5,3], [2,4,1,1,3]))
# print(el)
# el.sort(reverse=True)
# print(el)

print('Largest Rectangle in Histogram')

def largest_rectangular_area(heights):
  max_area = 0
  for i in range(len(heights) - 1):
    max_height = min(heights[i], heights[i + 1])
    temp_area = max_height * 2
    max_area = max(max_area, temp_area)

  for i in range(len(heights)):
    max_area = max(max_area, heights[i])
  
    
  return max_area

print(largest_rectangular_area([2,1,2]))

print("Valid Sudoku")
def valid_sudoku(board):
  print(len(board))
  # for row_index in range(len(board)):
  #   check = {}
  #   cols = {}
  for row_idx in range(9):
    nums_set = set()
    for i in range(9):
      if board[row_idx][i] in nums_set:
        return False
      elif board[row_idx][i] != ".":
        nums_set.add(board[row_idx][i])
    print('ROWS - ',nums_set)
  
  for cols_idx in range(9):
    cols_set = set()
    for i in range(9):
      if board[i][cols_idx] in cols_set:
        return False
      elif board[i][cols_idx] != ".":
        cols_set.add(board[i][cols_idx])
    print('Cols - ', cols_set)
  
  # Check the first box
  for square in range(9):
    box_set = set()
    for i in range(3):
      for j in range(3):
        row = (square//3 * 3) + i
        col = (square % 3 * 3) + j
        if board[row][col] in box_set:
          return False
        elif board[row][col] != ".":
          box_set.add(board[row][col])
    print('square 1 - ', box_set)
  return True
  

b = [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]

valid_sudoku(b)