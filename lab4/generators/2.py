def even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
x=int(input())
y=list(even(x))
for i in range(len(y)):
    if i==len(y)-1:
        print(y[i])
    else:
        print(y[i], end=", ")