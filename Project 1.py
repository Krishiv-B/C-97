import random
value=random.randint(1, 9)
print("Welcome to the number guesing game!!")
print("Guess a number between 1 and 9")
randomnumber=int(input("Enter your guess :- "))
i=1
while i<5:
    i=i+1
    if randomnumber<value:
        print("Your guess was low. Guess a number higher than", randomnumber)
        randomnumber=int(input("Enter your guess :- "))
    if randomnumber>value:
        print("Your guess was high. Guess a number lower than", randomnumber)
        randomnumber=int(input("Enter your guess :- "))
    if randomnumber==value:
        print("CONGRATULATIONS You Won!!")
        break
    
if not i < 5:
    print("You Lose!! The number was ", value) 
