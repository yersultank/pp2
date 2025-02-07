from random import randint
def guess_the_number():
    print("Hello! What is your name?")
    name=input()
    print(f"Well, {name} , I am thinking of a number between 1 and 20.")
    number=randint(1,20)
    cnt=0
    while True:
        guess=int(input("Take a guess."))
        cnt+=1
        if guess==number:
            print(f"Good job, {name}! You guessed my number in {cnt} guesses! ")
            break
        elif guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

guess_the_number()