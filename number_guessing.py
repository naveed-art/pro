# import random

# top_of_range = input("Type a number: ")
# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)

#     if top_of_range <=0:
#         print("please type a number larger than 0 next time.")
#         quit()
# else:
#     print("please type a number next time.")
#     quit()

# random_number= random.randint(0,top_of_range)
# # print (random_number)
# guesses = 0

# while True:
#     guesses +=1
#     user_guess = input("Make a guess: ")
#     if user_guess.isdigit():
#         user_guess = int(user_guess)
#     else:
#         print("please type a number next time.")
#         continue
#     if user_guess == random_number:
#         print("You got it!")
#         break
#     elif user_guess > random_number:
#         print("you were above the number!")
#     else:
#         print("you were below the number!")

# print("You got it in",guesses,"guesses")


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