# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def pronic(num):
        if(num==0 or num==2 or num==6):
                return True
        n=num//2
        for i in range(n):
                if(num==i*(i+1)):
                        return True
        return False

def nthpronicnumber(n):
	# Your code goes here
	fnd=0
	gt=-1
	while(fnd<=n):
		gt +=1
		if(pronic(gt)):
			fnd +=1
	return gt
