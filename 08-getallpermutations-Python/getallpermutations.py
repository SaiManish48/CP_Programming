# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def getallpermutations(x):
  if(len(x)==0):
        return []
  elif(len(x)==1):
    return x
  l=[]
  for i in range(len(x)):
    s=tuple(x[i])
    rem=x[:i]+x[i+1:]
    for j in getallpermutations(rem):
      j=tuple(j)
      t=s+j
      l.append(t)
  return l
