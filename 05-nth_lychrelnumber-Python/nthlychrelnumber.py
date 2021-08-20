# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def reverse(x):
  n=0
  while x>0:
    n=n*10+x%10
    x=x//10
  return n

def isPalindrome(n):
  return reverse(n) == n

def isLychrel(n):
  for i in range(50):
    n+=reverse(n)
    if isPalindrome(n):
      return False
  return True

def nthlychrelnumbers(n):
  cnt=0
  for i in range(4000):
    if(isLychrel(i)):
      cnt+=1
    if(cnt==n):
      break
  return i
