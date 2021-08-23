# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
        M=L
        sumofrow=[]
        for i in range(len(M)):
                sum=0
                for j in range(len(M[0])):
                        sum+=M[i][j]
                sumofrow.append(sum)
        rows=sumofrow.count(sumofrow[0])==len(sumofrow)
        print(sumofrow,len(sumofrow),rows)
        if(rows):
                #column
                sumofcol=[]
                for i in range(len(M[0])):
                        sum=0
                        for j in range(len(M)):
                                sum+=M[j][i]
                        sumofcol.append(sum)
                        # print(sumofrow,sumofcol)
                cols=sumofcol.count(sumofcol[0])==len(sumofcol)
                if(cols):
                        #diagonal
                        d1=0
                        d2=0
                        for i in range(len(M)):
                                d1+=M[i][i]
                                d2+=M[i][-1-i]
                        if(d1!=d2):
                                return True

        else:
                rowdict=dict((i,sumofrow.count(i)) for i in sumofrow)
                rwrong=min(rowdict,key=rowdict.get)
                rcorrect=max(rowdict,key=rowdict.get)
                diffr=rwrong-rcorrect
                for i in range(len(sumofrow)):
                        if(sumofrow[i]==rwrong):
                                flag1=i
                                #column
                sumofcol=[]
                for i in range(len(M[0])):
                        sum=0
                        for j in range(len(M)):
                                sum+=M[j][i]
                        sumofcol.append(sum)
                # print(sumofrow,sumofcol)
                cols=sumofcol.count(sumofcol[0])==len(sumofcol)
                if(cols):
                        #diagonal
                        d1=0
                        d2=0
                        for i in range(len(M)):
                                d1+=M[i][i]
                                d2+=M[i][-1-i]
                        if(d1!=d2):
                                return True
                else:
                        coldict=dict((i,sumofcol.count(i)) for i in sumofcol)
                        cwrong=min(coldict,key=rowdict.get)
                        ccorrect=max(coldict,key=rowdict.get)
                        diffc=cwrong-ccorrect
                        for i in range(len(sumofcol)):
                                if(sumofcol[i]==cwrong):
                                        flag2=i
                        if(diffr==diffc):
                                M[flag1][flag2]=M[flag1][flag2]-diffr
        return M
