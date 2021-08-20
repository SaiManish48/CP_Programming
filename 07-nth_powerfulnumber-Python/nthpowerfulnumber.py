# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math

def prime(n):
        if(n==2):
                return True
        elif(n<2 or n%2==0):
                return False
        num=round(math.sqrt(n))
        for i in range(3,num+1,2):
                if(n%i==0):
                        return False
        return True

def pwrnum(num):
        if(num==1):
                return True
        cnt=0
        cnt1=0
        for i in range(2,(num//2)+1):
                if(num%i==0 and prime(i)):
                        cnt +=1
                        if(num % (i*i)==0):
                                cnt1 +=1
        if( cnt ==0 and cnt1==0):
                return False
        elif( cnt==cnt1):
                return True
        else:
                return False


def nthpowerfulnumber(n):
        fnd=0
        ps=0
        while(fnd<=n):
                ps +=1
                if(pwrnum(ps)):
                        fnd +=1
        return ps
