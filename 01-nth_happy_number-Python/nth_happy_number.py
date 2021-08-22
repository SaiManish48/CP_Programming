# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)

def sumofsquares(n):
        sumofsquare=0
        while(n):
                sumofsquare=sumofsquare+((n%10)*(n%10))
                n=int(n/10)
        return sumofsquare

def ishappynumber(n):
  start=n
  stop=n
  while(True):
    start=sumofsquares(start)
    stop=sumofsquares(sumofsquares(stop))
    if(start!=stop):
      continue
    else:
      break
  if(start==1):
    return True
  else:
    return False
  
def nth_happy_number(n):
  found=1
  got=0
  while(found<=n):
    if(ishappynumber(got)):
      found+=1
    got+=1
  return got-1
