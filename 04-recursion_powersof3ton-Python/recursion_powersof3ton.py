# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 

def wrapper(l1,l2):
  empty=[]
  final=3**l2
  if(final<=l1):
    empty.append(final)
    return empty+wrapper(l1,l2+1)
  else:
    return empty
    
def recursion_powersof3ton(n):
  k=int(n)
  empty=[]
  if(k<=0):
    return None
  if(n==1):
    empty.append(k)
    return empty
  else:
    return wrapper(k,0)
