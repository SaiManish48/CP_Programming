# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


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

def fun_nth_kaprekarnumber(n):
    fnd=0
    guess=0
    while(fnd<=n):
        guess +=1
        if(kaprekar(guess)):
            fnd +=1
    return guess