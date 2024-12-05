
def permutate(s, path="", used=None):
  
  if used is None:
    used = [False] * len(s) #keep track of used letters
  
  #base case if current path contains all characters
  if len(path) == len(s):
    print(path)
    return
  
  #recursive case: try each characters
  for i in range(len(s)):
    if not used[i]:
      used[i] = True
      permutate(s, path + s[i], used)
      used[i] = False


print("String permutations")
permutate('nzo', "", None)