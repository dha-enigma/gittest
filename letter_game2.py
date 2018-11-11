import randomm
import sys
import os


words = [
    'apples',
    'bannana',
    'orange',
    'coconut',
    'strawberry',
    'lime',
    'grapefruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
    clear()

    print('Strikes {}/7'.format(len(bad_guesses)))
    print('')
    for letter in bad_guesses:
        print(letter, end=' ')
    print('\n\n')
    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')
                
    print('')
    
def get_guess(bad_guesses, good_guesses):
    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess

def play(done):
    clear()
    secret_word = random.choice(word)
    good_guesses = []
    bad_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word) 
        guess = get_guess(good_guesses,bad_guesses)
        
        if guess in secret_word:
            good_guesses.append(guess)
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            if found:
                print('You Win!')
                print("The secret word was {}".format(secret_word)
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses, good_guesses, secret_word)
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True
        
        if done:
            play_again = input("Play again Y/n: ").lower()
            if play_again != 'n':
                return play(done = False)
            else:
                sys.exit()

def wlcome():
    start = input("Press Enter or Return to start or Enter Q to quit: ").lower()
    if start = 'q':
        print('Bye!')
        sys.exit()
    else:
        return True

print('Welcome to Letter Game!')

done = False

While True:
clear()
welcome()






