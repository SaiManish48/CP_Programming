"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # Your code goes here
    l=0
    h=len(input_array)-1
    m=0
    while(l<=h):
        m=(l+h)//2
        if(input_array[m]<value):
            l=m+1
        elif(input_array[m]>value):
            h=m-1
        else:
            return m
    return -1
