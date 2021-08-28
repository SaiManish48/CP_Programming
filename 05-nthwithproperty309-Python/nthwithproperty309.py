# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def proprty(n):
        num='0123456789'
        ans=str(n**5)
        for i in num:
                if i not in ans:
                        return False
        return True

def nthwithproperty309(n):
        fnd=0
        guess=308
        while(fnd<=n):
                guess +=1
                if(proprty(guess)):
                        fnd +=1
        return guess

print(nthwithproperty309(0))