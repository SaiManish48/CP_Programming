# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.

def iseven(n,i=0,null=0):
        if(n==0):
                return null
        tmp=n%10
        if(tmp%2==0):
                null +=(10**i*tmp)
                i +=1
        return iseven(n//10,i,null)

def fun_recursion_onlyevendigits(l):
        lst=[]
        if(len(l)==0):
                return lst
        else:
                evn=iseven(l[0])
                lst.append(evn)
                return lst+fun_recursion_onlyevendigits(l[1:])
