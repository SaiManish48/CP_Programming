# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

# Prerequisite for the following problem is the above problem.
# Write the function inverseLookAndSay(a) that does the inverse of the above problem, so that, in general:
#       inverseLookAndSay(lookAndSay(a)) == a
# Or, in particular:
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([]) == []
# inverseLookAndSay([(3,1)]) == [1,1,1]
# inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7]
# inverseLookAndSay([(2,3),(1,8),(3,-10)]) == [3,3,8,-10,-10,-10]
# inverseLookAndSay([(2,3),(1,8),(4,3)]) == [3,3,8,3,3,3,3])

def inverselookandsay(a):
        temp=[]
        if(len(a[0])==0):
                return []
        else:
                for i in range(len(a)):
                        s=a[i][0]
                        for j in range(s):
                                temp.append(a[i][1])
        return temp

def lookAndSay(a):
  leng=len(a)
  if(leng==0):
    return []  
  count=1  
  empty=[] 
  for singl in range(leng-1):
    if(a[singl]==a[singl+1]):
      count=count+1
    else:
      empty.append((count,a[singl]))
      count=1
  empty.append((a[leng-1]),count)
  return empty
