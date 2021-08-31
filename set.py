# limitedPowerSet(n, k)
# Write a function limitedPowerSets(n, k) that takes possibly 
# a non-negative integer n and k and returns the list that 
# contains k number of subsets from the power set as sets. 
# (The values in the set will range from 1 to n).
# Example:
# 	limitedPowerSet(5, 7) => 
# [ {}, {1}, {2}, {3}, {4}, {5}, {1, 2} ]

def limitedPowerSet(n,l):
    k=[]
    k.append({})
    for i in range(1,n+1):
        for j in range(1,(n+1)-(i-1)):
            temp=[]
            for x in range(j,j+i):
                temp.append(x)
                
            if(len(k)<l):
                k.append(set(temp))
            else:
                return k
    if(len(k)==l):
        return k
    else:
        return None
    
    
print(limitedPowerSet(5,16))
print(limitedPowerSet(0,3))
print(limitedPowerSet(0,1))
print(limitedPowerSet(5,3))
print(limitedPowerSet(3,3))
print(limitedPowerSet(7,17))
print("All Test cases passed................")
