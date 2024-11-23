

def lengthOfLongestSubstring(self, s: str) -> int:
  seen_chars = set()
  max_length = 0
  left = 0
  right = 0
  
  while right <- len(s):
    
    if s[right] not in s:
      seen_chars.add(s[right])
      right += 1
    else:
      while s[right] in seen_chars:
        seen_chars.remove(s[left])
        left += 1
    
  
  
  # Brute force
  # if len(s) == 0:
  #   return 0
  # if len(s) == 1:
  #   return 1
  # for i in range(len(s)):
  #   for j in range(i, len(s), 1):
  #     print(i, j)
  #     if s[j] not in seen_chars:
  #       seen_chars.add(s[j])
  #     else:
  #       max_length = max(max_length, len(seen_chars))
  #       # print(seen_chars, max_length)
  #       seen_chars.clear()
  #       break
  return max_length

print("Longest Repeating Char wih Replacement")
def longest_repeating_character_replacement(s, k):
  max_length = 0
  current_char_max = 0
  chars_map = {}
  left = 0
  right = 0
  for i in range(len(s)):
    chars_map[s[right]] = 1 + chars_map.get(s[right], 0)
    current_char_max = max(current_char_max, chars_map[s[right]])
    if (right - left + 1) - current_char_max <= k:
      max_length = max(max_length, right - left + 1)
    else:
      while (right - left + 1) - current_char_max > k:
        chars_map[s[left]] = chars_map.get(s[left]) - 1
        current_char_max = max(current_char_max, chars_map[s[left]])
        left += 1
    right += 1
  return max_length
  
  # Brute force
  # result = 0
  # for i in range(len(s)):
  #   update_count = {}
  #   current_max_length = 0
  #   for j in range(i, len(s)):
  #     update_count[s[j]] = 1 + update_count.get(s[j], 0)
  #     current_max_length = max(current_max_length, update_count[s[j]])
  #     if (j - i + 1) - current_max_length <= k:
  #       result = max(result, j - i + 1)
  # return result
  # max_length = 0
  # for i in range(len(s)):
  #   repeating_chars = {}
  #   update_count = 0
  #   for j in range(i, len(s), 1):
  #     if repeating_chars.get(s[j]):
  #       repeating_chars.update({s[j]: repeating_chars.get(s[j]) + 1})
  #       print(repeating_chars)
  #     elif len(repeating_chars) == 0:
  #       repeating_chars[s[j]] = 1
  #     elif update_count != k:
  #       current_key = list(repeating_chars.keys())[0]
  #       repeating_chars.update({current_key: repeating_chars.get(current_key) + 1})
  #       update_count += 1
  #       print('UD', update_count)
  #     else:
  #       break
  #   print(repeating_chars)
  #   max_length = max(max_length, list(repeating_chars.values())[0])
  # return max_length   

# m = {}
# m['A'] = 1
# j = 'A'
# print(m)  
# print(m.get('D'))  
# print(m.get('A'))          
# print(list(m.keys())[0]) 
# m.update({j: m.get(j) + 1})
# print(list(m.values())[0])

print(longest_repeating_character_replacement('ABBB', 2))
# print(longest_repeating_character_replacement('AABABBA', 1))