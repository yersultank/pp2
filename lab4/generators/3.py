def func(n):
    for i in range(1, n):
        if i%3==0 and i%4==0:
            yield i
x=int(input())
y=func(x)
for i in y:
    print(i)
