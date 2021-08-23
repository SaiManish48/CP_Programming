# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	s=len(a)
  
	if(s==0 or s==1):
		return True
	
	elif(a[-1]>=a[0]):
		prev=a[0]
		for i in range(1,len(a)):
			if(prev>a[i]):
				return False
			prev=a[i]
		return True
	
	elif(a[0]>=a[-1]):
		final=a[-1]
		for i in range(2,len(a)+1):
			if(final>a[-i]):
				return False
			final=a[-i]
		return True
	
	else:
		return False