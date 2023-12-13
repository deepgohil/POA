def badd(L1,L2):
    result=[]
    carry=0
    for d1,d2 in zip(reversed(L1),reversed(L2)):
        sum=d1+d2+carry
        result.insert(0,sum%2)
        carry=sum//2
    return result    

Q=[1,0,0,0,1]
M=[0,0,0,0,1,1]
onesofM=[1,1,1,1,0,0]
minusM=[0,0,0,0,0,1]
AC=[0,0,0,0,0]
C=[0]

minusM=badd(onesofM,minusM)

# print(minusM)


resultList=[]
resultList.extend(C)
resultList.extend(AC)
resultList.extend(Q)

for i in range(3):
    resultList=resultList[1:] + [0]
    AC.insert(0,C[0])
    print(AC)
    AC=badd(AC,minusM)
    print()
    print(AC)
    resultList=[]
    resultList.extend(AC)
    resultList.extend(Q)
    if(resultList[0]==0):
        resultList[-1]=1
    if(resultList[0]==1):
        resultList[-1]=0
        AC=badd(resultList[:6],M)
    fnailresultList=[]
    fnailresultList.extend(AC)
    fnailresultList.extend(resultList[6:])
    print(fnailresultList)

