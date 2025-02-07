def histogram(mylist):
    for i in range(len(mylist)):
        print(mylist[i]* ("*"))
a=list(map(int,input("your list: ").split()))
histogram(a)