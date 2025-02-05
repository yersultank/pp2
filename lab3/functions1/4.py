def filter_prime(numbers):
    prime_list=[]
    for i in numbers:
        cnt=0
        for j in range(1,i+1):  
            if i%j==0:
                cnt+=1
        if cnt==2:
            prime_list.append(i)
    return prime_list

a=int(input("how many numbers: "))
numbers=list(map(int,input(f"Type {a} numbers separated by spaces:").split()))
result=filter_prime(numbers)
print(result)



