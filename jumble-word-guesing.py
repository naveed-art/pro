import random

words = ['science','python','java']
word = random.choice(words)

#for understanding
samp = random.sample(word,len(word))
print(samp)
samp = ''.join(samp)
print(samp)

jumble = ''.join(random.sample(word,len(word)))
print(f"the jumble word is {jumble}")

guess = input("Write your guess: ")

if guess == word:
    print("Correct")
    
else:
    print(f"Incorrecr: The word is {word}")


