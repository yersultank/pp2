class Bank:
    def __init__(self, user, money):
        self.user=user
        self.money=money
    
    def owner(self):
        print(self.user)
    
    def balance(self):
        print("There are ", self.money, " tenge on your balance")

    def deposit(self, money):
        self.money+=money
        print("you have replenished your balance by ", self.money)

    def withdraw(self, money):
        if self.money-money<0:
            print("insufficient funds on balance")
        else:
            self.money-=money
            print("you withdrew: ", money, " tenge from your account, you are left with: ", self.money)

mymoney=int(input())
myacc=Bank("Yersultan", mymoney)
myacc.owner()
myacc.balance()
myacc.deposit(int(input("type your deposit:")))
myacc.withdraw(int(input("type your withdraw:")))




         