# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.



def fun_kth_occurrences(s, n):
	tmp={}
	for i in s:
		if i not in tmp.keys():
			j=s.count(i)
			tmp[i]=j
	ky=list(tmp.keys())
	val=list(tmp.values())
	srt=sorted(tmp.values(),reverse=True)[n-1]
	l=val.index(srt)
	return (ky[l])
