def spy_game(mylist):
    cnt=0
    for i in range(len(mylist)-2):
        if mylist[i]==mylist[i+1]==0 and mylist[i+2]==7:
            cnt+=1
    return cnt>0

a=list(map(int,input("your list: ").split()))
print(spy_game(a))