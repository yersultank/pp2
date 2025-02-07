def check(mylist):
    cnt=0
    for i in range(len(mylist)-1):
        if mylist[i]==mylist[i+1]==3:
            cnt+=1
    return cnt > 0
arr=list(map(int,input("write numbers for a list: ").split()))
result=check(arr)
print(result)