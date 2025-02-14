def squares(n,m):
    for i in range(n,m+1):
        yield i**2
x=int(input())
y=int(input())
z=squares(x,y)
for i in z:
    print(i)