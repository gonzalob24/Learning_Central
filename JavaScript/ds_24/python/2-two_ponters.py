class Solution:
  def is_palindrome(self, s: str) -> bool:
    
    if len(s) == 0:
      return True
    right = len(s) - 1
    left = 0
    
    while left < right:
      while left < right and not s[left].isalnum():
        left += 1
      while right > left and not s[right].isalnum():
        right -= 1
      if s[left].lower() != s[right].lower():
        return False
      left += 1
      right -= 1
    return True

test = Solution()
print(test.is_palindrome("A man, a plan, a canal: Panama"))
# print(not ' '.isalnum())


def two_sum_2(numbers, target):
  # numbers is sorted in on-decreasing (increasing) order
  # target: target can be negative or positive
  # just assume all numbers
  # [] - 0, 12 --> 0
  # return the index of the two numbers that add up to target sum
  # [2,7,11,15], 9 --> [0, 1]
  # target = A + B
  # B (difference) =  target - current_number 
  # Your solution must use only constant extra space.
  #  seen_numbers = {} --> O(n)
  # for i in range(len(numbers)):
  #   difference = target - numbers[i]
  #   if not seen_numbers.get(difference) and seen_numbers.get(difference) != 0:
  #     seen_numbers[numbers[i]] = i + 1
  #   else:
  #     return [seen_numbers[difference], i + 1]
  left = 0
  right = len(numbers) - 1
  for i in range(len(numbers)):
    left_number = numbers[left]
    right_number = numbers[right]
    current_sum = left_number + right_number
    if current_sum == target:
      return [left + 1, right + 1]
    elif current_sum > target:
      right -= 1
    elif current_sum < target:
      left += 1
    
  return None

print("Two Sum 2")
print(two_sum_2([2,7,11,15], 9))
print(two_sum_2([-1, 0], -1))

def three_sum(nums): 
  nums.sort()
  result_set = []
  
  for i, num in enumerate(nums):
    if num > 0:
      break
    
    if i > 0 and num == nums[i - 1]:
      continue
    
    left = i + 1
    right = len(nums) - 1

    while left < right:
      three_sum = num + nums[left] + nums[right]
      if three_sum > 0:
        right -= 1
      elif three_sum < 0:
        left += 1
      else:
        result_set.append([num, nums[left], nums[right]])
        left += 1
        # right -= 1
        while nums[left] == nums[left - 1] and left < right:
          left += 1
  return result_set

print('Three Sum')
print(three_sum([-1,0,1,2,-1,-4]))
# s = set([1,2,3])
# print(s)
# print(list(s))

def max_area(height):
  max_area = 0
  right = len(height) - 1
  left = 0
  
  while left < right:
    min_height = min(height[left], height[right])
    width = right - left
    current_area = min_height * width
    max_area = max(max_area, current_area)
    
    if min_height == height[left]:
      left += 1
    else:
      right -= 1
    
  return max_area

  # Brute force
  # max_area = 0
  # for i, h in enumerate(height):
  #     for j in range(len(height) - 1):
  #         j = j + 1
  #         min_height = min(h, height[j])
  #         width = j - i
  #         current_area = min_height * width
  #         max_area = max(max_area, current_area)
  # return max_area
      
print('Container with most water')
print(max_area([1,8,6,2,5,4,8,3,7]))


print('Trapping Rain Water')

def trapping_rain_water(height):
  left = 0
  right = len(height) - 1
  max_area = 0
  left_max = height[left]
  right_max = height[right]
  while left < right:
    print('points -- ', left, right)
    if left_max < right_max:
      left += 1
      left_max = max(left_max, height[left])
      max_area += left_max - height[left]
    else:
      right -= 1
      right_max = max(right_max, height[right])
      max_area += right_max - height[right]
    print('area -- ', max_area)
    
  return max_area
    
print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))