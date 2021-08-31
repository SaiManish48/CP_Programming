# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    if(len(lst)==0):
        return False
    temp=[i for i in range(1,len(lst)+1)]
    for i in range(len(lst)):
        for j in temp:
            if j not in lst[i]:
                return False
    for i in range(len(lst[0])):
        te=[]
        for j in range(len(lst)):
            te.append(lst[j][i])
        for k in temp:
            if k not in te:
                return False
    return True
        
            
assert(isLatinSquare([[1,2,3],[2,3,1],[3,1,2]])==True)
assert(isLatinSquare([[1,1,1],[1,1,1],[0,0,0]])==False)
assert(isLatinSquare([[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]])==True)
assert(isLatinSquare([])==False)
assert(isLatinSquare([[1,2,3],[4,5,6],[7,8,9]])==False)
print("All Test cases passed..................")
