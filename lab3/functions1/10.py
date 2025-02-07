def uniquelist(mylist):
    newlist=[]
    newlist.append(mylist[0])
    for i in range(len(mylist)):
        cnt=0
        for j in range(len(newlist)):
            if mylist[i]==newlist[j]:
                cnt+=1
        if cnt==0:
            newlist.append(mylist[i])
    return newlist

a=list(map(int,input("your list: ").split()))
print(uniquelist(a))

