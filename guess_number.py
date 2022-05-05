import random

range_num = input("Enter range num: ")
if range_num.isdigit():
    range_num = int(range_num)
    
else:
    print("enter a valid number next time")
    quit()
    
random_num = random.randint(0,range_num)
guesses = 0
while True:
    guesses +=1
    guess = input("Enter guess num: ")
    if guess.isdigit():
        guess = int(guess)
        if guess == random_num:
            print("Congratz! your number matched")
            break
        elif guess < random_num:
            print("Enter a larger num")
            continue
        else:
            print("Enter a smaller num")
            continue
    else:
        print("Enter a number next time")
        
        
print("You got it",guesses,"guesses")
