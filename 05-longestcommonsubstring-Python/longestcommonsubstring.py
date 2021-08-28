# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    fnl=""
    l1=len(s2)
    l2=len(s1)
    for i in range(l1):
        smlar=''
        for j in range(l2):
            if(i+j<l1 and s2[i+j]==s1[j]):
                smlar+=s1[j]
            else:
                if(len(smlar)>=len(fnl)):
                    fnl=smlar
                    smlar=""
    return fnl
