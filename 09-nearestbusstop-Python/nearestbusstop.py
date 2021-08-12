# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.


def fun_nearestbusstop(street):
	a=street//8
	n1=8*a
	n2=8*(a+1)
	s1=abs(n1-street)
	s2=abs(n2-street)
	if(s1>s2):
    		return n2
	else:
    		return n1
