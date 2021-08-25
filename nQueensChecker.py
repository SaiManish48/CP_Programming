# nQueensChecker(a)
# Background: The "N Queens" problem asks if we can place N queens on an NxN chessboard such that no two queens are attacking each other. For most values of N, there are many ways to solve this problem. Here, you will write the function nQueensChecker(board) that takes a 2d list of booleans where True indicates a queen is present and False indicates a blank cell, and returns True if this NxN board contains N queens all of which do not attack any others, and False otherwise.

def nQueensChecker(a):
    for i in range(len(a)):
        if(a[i].count(True)!=1):
            return False
    for j in range(len(a[i])):
        temp=[]
        for k in range(len(a[i])):
            temp.append(a[k][j])
        if(temp.count(True)!=1):
            return False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j]==True):
                x=i
                y=j
                while(x!=len(a)-1 and y!=len(a)-1):
                    if(a[x][y]==True  and x!=i and y!=j):
                        return False
                    x+=1
                    y+=1
                while(x!=len(a)-1 and y!=0):
                    if(a[x][y]==True  and x!=i and y!=j):
                        return False
                    x+=1
                    y-=1
    return  True
                    
                    
assert(nQueensChecker([[False,True,False,False],[False,False,False,True],[True,False,False,False],[False,False,True,False]])==True)
assert(nQueensChecker([[False,True,False,False],[False,False,False,False],[True,False,False,False],[False,False,False,False]])==False)
assert(nQueensChecker([[False,False,True,False],[True,False,False,False],[False,False,False,True],[False,True,False,False]])==True)
print("All Test Cases Passed")

#https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/
