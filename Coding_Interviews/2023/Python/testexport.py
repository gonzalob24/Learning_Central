def add(a, b):
  return a + b

def sumOfAllOddIntsSmallerThanN(n):
  
  sumOfOdds  = 0
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    for num in range(1, n + 1, 2):
      sumOfOdds = sumOfOdds + (num*num);
    return sumOfOdds