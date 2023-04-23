# Coming up with the Idea:

# The rules of Bulls and Cows:
# 1. The game is played with a 4-digit number, in which each digit is unique.
# 2. The computer chooses a random number, which the player tries to guess.
# 3. The player makes a guess by entering a 4-digit number.
# 4. If the player guesses a digit that is in the correct position in the
# chosen number, it is called a "bull".
# 5. If the player guesses a digit that is in the chosen number, but in a
# different position, it is called a "cow".
# 6. The computer responds to each guess with the number of bulls and cows.
# For example, if the chosen number is 4827 and the player guesses 1234, the
# computer would respond with "0 bulls, 2 cow" because the player guessed the
# digit 2, which is in the chosen number, but in a different position.
# 7. The player continues to guess until they correctly guess the entire
# number (i.e., four bulls).
from random import randint


def game_rules():
    print('''
-------------------------------------------------------------------------
Welcome to brainstorming BULLS AND COWS GAME!!!
-------------------------------------------------------------------------
The rules of Bulls and Cows:
1. The game is played with a 4-digit number, in which each digit is unique.
2. The computer chooses a random number, which the player tries to guess.
3. The player makes a guess by entering a 4-digit number.
4. If the player guesses a digit that is in the correct position in the
chosen number, it is called a "bull".
5. If the player guesses a digit that is in the chosen number, but in a
different position, it is called a "cow".
6. The computer responds to each guess with the number of bulls and cows.
For example, if the chosen number is 4827 and the player guesses 1234, the
computer would respond with "0 bulls, 2 cow" because the player guessed the
digit 2, which is in the chosen number, but in a different position.
7. The player continues to guess until they correctly guess the entire
number (i.e., four bulls).
-------------------------------------------------------------------------
The computer has just generated a number that you need to guess. Give it a try!
-------------------------------------------------------------------------''')


game_rules()


def number_generator():
    generated_number = []
    '''
    Function generates 4-digit number (list of 4 random unique digits)
    '''
    while len(generated_number) < 4:
        a = randint(0, 9)
        if a not in generated_number:
            generated_number.append(a)
    return generated_number


secret_number = number_generator()
print(secret_number)


class Guess:
    '''
    Main Guess class. It takes two lists as parameters during initialization.
    The first parameter is passed as an argument when creating an instance of
    the class, which is based on user input. The second parameter, by default,
    contains a list of digits of the secret number.
    Contains class attribute guess_list which adds to list instance attributes
    after each initialization

    '''
    guess_list = []

    def __init__(self, my_guess, secret):
        self.my_guess = my_guess
        self.secret = secret
        Guess.guess_list.append(self)

    def bull_counter(self):
        '''
        Counts the number of digits that are in the correct position
        '''
        bull_counter = 0
        for i in range(4):
            if self.my_guess[i] == self.secret[i]:
                bull_counter += 1
        return bull_counter

    def cow_counter(self):
        '''
        Counts the number of digits that are in the chosen number
        '''
        cow_counter = 0
        for i in range(4):
            if (self.my_guess[i] in self.secret) and (
                    self.my_guess[i] != self.secret[i]):
                cow_counter += 1
        return cow_counter

    def show_all_scores(self):
        '''
        Generates a dictionary of guess/score pairs as key|value pairs
        '''
        all_scores = {}
        for i in Guess.guess_list:
            guess_string = ''.join(str(num) for num in i.my_guess)
            all_scores[guess_string] = [i.bull_counter(), i.cow_counter()]
            print(f'{"-".join(str(num) for num in i.my_guess)} | '
                  f'{"-".join(str(num) for num in [i.bull_counter(), i.cow_counter()])}')
        return all_scores


guess_list = []


def get_guess():
    '''
    Receives guess number from the User.
    The loop will repeatedly request data, until it is valid.
    '''
    while True:
        guess_string = input(
            '''Please make your guess, input your 4-unique digit number:
-------------------------------------------------------------------------\n''')
        if validate_guess(guess_string):
            break
    # converting user input (numerical string) into a list of numbers
    users_guess = [int(num) for num in list(guess_string)]
    guess = Guess(users_guess, secret_number)
    guess_list.append(guess_string)
    return guess


def validate_guess(values):
    '''
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 4 values.
    '''
    try:
        if len(values) != 4 and len(values) != 0:
            raise ValueError(
                f'Exactly 4 values required, you provided {len(values)}')
    except ValueError as err:
        print(f'Invalid data: {err}, please try again.\n')
        return False

    try:
        if len(values) == 0:
            raise ValueError('You should not leave an empty field as your input.')
    except ValueError as err:
        print(f'{err}\n')
        return False

    try:
        if len([i for i in values if not i.isdigit()]) > 0:
            raise ValueError(' , '.join([i for i in values if not i.isdigit()]))
    except ValueError as err:
        print(f'Your input should be a four-digit number with unique digits, but it has {err} sign(s) instead.')
        return False

    try:
        if values in list(guess_list):
            raise ValueError(values)
    except ValueError as err:
        print(f'You have already make this guess: {err}. Try again please.')
        return False

    try: 
        if len(values) != len(set(values)):
            raise ValueError(' and '.join(str(x) for x in set([i for i in values if values.count(i) > 1])))
    except ValueError as err:
        print(f'You have repetetive digit(s) in your guess: {err}. Try again please.')
        return False

    return True


def main():
    while True:
        guess = get_guess()
        guess.show_all_scores()
        if guess.bull_counter() == 4:
            break
    print('''
Congratulations! You win!!!
Input Y if you want to play again. 
To quit the game input N
''')
    users_choice = input()
    if users_choice.lower() == 'y':
        main()
    elif users_choice.lower() == 'n':
        return


main()


