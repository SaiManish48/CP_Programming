# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 


def printPascal(n):
        matrix=[]
        for line in range(0, n):
                a=[]
                for i in range(0, line + 1):
                        a.append(binomialCoeff(line, i))
                matrix.append(a)
        return matrix
     
def binomialCoeff(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
     
    return res



def fun_pascaltrianglevalue(row, col):
	a=printPascal(row+1)
	for i in range(len(a)):
		for j in range(i+1):
			if(i==row and j==col):
				return a[i][j]
			else:
				continue
	return 0
