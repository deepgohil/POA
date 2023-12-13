def badd(minusM,dummy):
    result=[]
    carry=0
    for d1,d2 in zip(reversed(minusM),reversed(dummy)):
        sum=d1+d2+carry
        result.insert(0,sum%2)
        carry=sum//2
    return result    


# m=[]
# q=[]

# m=input("enter M :").split()
# q=input("enter Q :").split()

# for i in m:
#     val=int(m.pop(0))
#     m.append(val)
# for i in q:
#     val=int(q.pop(0))
#     q.append(val)    

# minusM=[]

# for i in m:
#     if(i==0):
#         minusM.append(1)
#     else:
#         minusM.append(0)    

# dummy=[]
# for i in m:
#     dummy.append(0)
# dummy.pop()
# dummy.append(1)   

# print(f"m={m}")
# print(f"Q={q}")
# print(f"once complement of m {minusM}")
# print(f"dummy dats for 2s comp {dummy}")
M=[0,1,1,1]
minusM = [1,0,0,1]
dummy = [0, 0, 0, 1]
QDATA=[1,1,0,1]
QMINONE=[0]
A=[0,0,0,0]

# minusM=badd(minusM,dummy)

print(f"result twos comp=  {minusM}")

for i in range(4):
    if(QDATA[-1]==1 and QMINONE[0]==0):
        A=badd(A,minusM)
    if(QDATA[-1]==0 and QMINONE[0]==1):
        A=badd(A,M)
    resultList=[]
    resultList.extend(A)
    resultList.extend(QDATA)
    resultList.extend(QMINONE)
    print(resultList)
    resultList=[resultList[0]]+resultList[:-1]
    print("result list")
    print(resultList)
    A=resultList[:4]
    QDATA=resultList[4:8]
    QMINONE=resultList[8:]








