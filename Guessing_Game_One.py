import random
guess = ''
while (1):
    a = random.randint(1,9)
    guess = input("Guess a number betweeen 1 and 9:")
    try:
        if int(guess) - a == 0:
            print("Congrats you've guess it correct!")
            print("The answer is :", a)
        elif (int(guess) - a) in range (-1,-3):
            print("You got near to it")
            print("The answer is :", a)
        elif (int(guess) - a) in range (1,3):
            print("You got near to it")
            print("The answer is :", a)
        else:
            print("Oops Try Agian")
            print("The answer is :", a)
    except:
        if guess == 'exit':
            break
        else:
            print("Check Your Input")
print("Thank You For playing")