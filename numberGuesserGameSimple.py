import random

def guesser(secret):
    yourGuess = None
    count = 0
    '''
    Run this game until the user guesses the correct number
    '''
    while yourGuess != secret:
        yourGuess = input("\nEnter your guess: ")
        '''
        Check if user input is an integer
        '''
        if yourGuess.isdigit():
            yourGuess = int(yourGuess)
            '''
            Check if user input matches the secret random value. If it's incorrect, check is the guess is higher or 
            lower than the secret value.
            '''
            if yourGuess != secret and yourGuess < secret:
                print("Wrong guess!\nThe secret number is larger than your guess.")
            elif yourGuess != secret and yourGuess > secret:
                print("Wrong guess!\nThe secret number is smaller than your guess.")
            else:
                print("Right guess!\n")
        else:
            print("Your guess is not an integer, please re-enter an integer value.\n")
        '''
        Regardless if the user got the format right or wrong, it will count as a guess. 
        Increment the count value to return at the end.
        '''
        count += 1
    return count


if __name__ == '__main__':
    print("Welcome to your number guesser game!\n")
    maxValue = None
    '''
    Check if user input is an integer using try/catch to catch ValueErrors if input is in the incorrect format
    '''
    while maxValue is None:
        try:
            maxValue = int(input("Enter the maximum value for your guessing range: "))
        except ValueError:
            print("Your maximum value is not an integer, please re-enter an integer value.\n")
    '''
    Once the user input is an integer, use that input to get the random value. Then call the guesser game function.
    '''
    secretNumber = random.randint(0, maxValue)
    print("It took you %d guess(es) to guess the number %d!" % (guesser(secretNumber), secretNumber))
