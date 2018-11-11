import random


def game():
    #Generate random number
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 3:
        try:
            #Get a number guess from player
            guess = int(input("Guess a number between 1 and 10: "))
        except:
            print("{} is not a number".format(guess))
        else:
            #compare guess to secret num
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num)) 
                break
            elif guess < secret_num:
                print("My number is higher than that")
            else: 
                print("My number is lower than that")
            guesses.append(guess)
    else:
        print("You didn't get it! My number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n: ")
    if play_again != 'n':
        game()
    else:
        print("Bye!")

game()