import random
from hangman_art import logo, stages
from hangman_words import word_list
print(logo)

chosen_word = random.choice(word_list)
display = []
wordlen = len(chosen_word)
lives = 6 

for i in chosen_word:
    display.append("_")

print(chosen_word)
print(display)

statement = False


while(not statement):
    guess = input("Guess a letter : ")
    # to clear screen
    clear = "\n"*100
    print(clear)
    if guess in display:
        print("You have already guessed this letter.")
    for position in range(wordlen):
        if(chosen_word[position] == guess):
            display[position] = guess
            # print(lives)
    print(display)  

    if guess not in chosen_word:
        print("You have guessed a wrog letter. Try Again")
        lives -= 1
        if lives == 0:
            statement = True
        print(stages[lives])    

    if("_" not in display):
        statement = True
        print("you won!")
    