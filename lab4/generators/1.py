def square(n):
    cnt=1
    while cnt<=n:
        yield cnt**2
        cnt+=1
x=int(input())
y=square(x)
for i in y:
    print(i)