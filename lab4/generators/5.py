def func(n):
    while n!=-1:
        yield n
        n-=1
x=int(input())
y=func(x)
for i in y:
    print(i)