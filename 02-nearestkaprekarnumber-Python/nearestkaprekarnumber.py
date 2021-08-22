# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def kaprekar(n):
    y=n**2
    i=0
    sum=0
    while(y>0):
        rem=y%10
        y=y//10
        sum=sum+(rem*pow(10,i))
        if(sum!=0 and y+sum==n):
            return True
        i+=1
    return False

def fun_nearestkaprekarnumber(n):
    count=1
    if(kaprekar(n)):
        return n
    while(True):
        a=n+count
        b=n-count
        if(kaprekar(b)):
            return b
        elif(kaprekar(a)):
            return a
        count+=1