# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def ismostlymagicsquare(a):
	# Your code goes here
	s1=[]
	for i in a:
		s1.append(sum(i))
	s=0
	for j in range(len(a)):
		for k in range(len(a)):
			s=s+a[j][k]
		s1.append(s)
		s=0
	sm2=sm1=0
	for x in range(len(a)):
		sm2=sm2+a[x][x]
		sm1=sm1+a[x][len(a)-1-x]
	s1.append(sm2)
	s1.append(sm1)

	if(len(set(s1))==1):
		return True
	else:
		return False