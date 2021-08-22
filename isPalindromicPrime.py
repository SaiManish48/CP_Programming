def isaprime(x):
  if(x<2):
    return False
  if(x==2):
    return True
  if(x%2==0):
    return False
  maximfactor=round(x**0.5)
  for k in range(3,maximfactor+1,2):
    if(x%k==0):
      return False
  return True

def palindrome(x):
  tempo=x
  reversetemp=0
  while(x>0):
    digit=x%10
    reversetemp=(reversetemp*10)+digit
    x=x//10
  if(tempo==reversetemp):
    return True
  else:
    return False  
		
def ispalindromicprime(x):
  return (isaprime(x) and palindrome(x))


assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed")
