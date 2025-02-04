class prime:
    def __init__(self,numbers):
        self.numbers=numbers

    def is_prime(self,number):
        cnt=0
        for i in range(1,number+1):
            if number%i==0:
                cnt+=1
        if cnt==2:
            return True
        else:
             return False
        
    def filter(self):
        return list(filter(lambda x: self.is_prime(x), self.numbers))

a=int(input("how many numbers to check:"))
arr=[]
for i in range(1,a+1):
    n=int(input("type a number:"))
    arr.append(n)

myfilter=prime(arr)
print(myfilter.filter())

