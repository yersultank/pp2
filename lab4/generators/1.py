#1 task
# def square(n):
#     cnt=1
#     while cnt<=n:
#         yield cnt**2
#         cnt+=1
# x=int(input())
# y=square(x)
# for i in y:
#     print(i)

#2 task
# def even(n):
#     for i in range(0,n+1):
#         if i%2==0:
#             yield i
# x=int(input())
# y=list(even(x))
# for i in range(len(y)):
#     if i==len(y)-1:
#         print(y[i])
#     else:
#         print(y[i], end=", ")

#3 task
# def func(n):
#     for i in range(1, n):
#         if i%3==0 and i%4==0:
#             yield i
# x=int(input())
# y=func(x)
# for i in y:
#     print(i)

#4 task
# def squares(n,m):
#     for i in range(n,m+1):
#         yield i**2
# x=int(input())
# y=int(input())
# z=squares(x,y)
# for i in z:
#     print(i)

#5 task
# def func(n):
#     while n!=-1:
#         yield n
#         n-=1
# x=int(input())
# y=func(x)
# for i in y:
#     print(i)