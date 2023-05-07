'''
This module contains code for the Bulls and Cows game
'''
from random import randint
from colorama import Fore, Back, Style

DEBUG = False


# COLOR VARIABLES

ILINE_COLOR = Fore.LIGHTBLUE_EX
RULES_COLOR = Fore.LIGHTYELLOW_EX
ERR_COLOR = Fore.RED
WIN_BCOLOR = Back.RED
WIN_FCOLOR = Fore.LIGHTWHITE_EX
VARIABLE_COLOR = Fore.LIGHTYELLOW_EX
MAKE_GUESS = Fore.LIGHTGREEN_EX
DIM = Style.DIM
RESET_ALL = Style.RESET_ALL


def game_rules():
    '''
    Prints rules of the game in the terminal
    '''
    print(
        ILINE_COLOR +
        '''-------------------------------------------------------------------
Welcome to brainstorming BULLS AND COWS GAME!
-------------------------------------------------------------------'''
        + RESET_ALL)
    print(
        ILINE_COLOR +
        '''+-++-++-++-++-+ +-++-++-+ +-++-++-++-+
|B||U||L||L||S| |A||N||D| |C||O||W||S|
+-++-++-++-++-+ +-++-++-+ +-++-++-++-+
-------------------------------------------------------------------'''
        + RESET_ALL)
    print(
        ILINE_COLOR +
        '''Doubles the energy of your morning cup of coffee!!!
-------------------------------------------------------------------'''
        + RESET_ALL)
    print(RULES_COLOR + '''The rules of Bulls and Cows:

1. The game is played with a four unique-digit number.
2. The computer generates a random number for the player to guess.
3. The player makes a guess by entering a 4-digit number.
4. If the player guesses a digit that is in the correct position in
the chosen number, it is called a "bull".
5. If the player guesses a digit that is in the chosen number, but
in a different position, it is called a "cow".
6. The computer responds to each guess with the number of bulls
and cows. For example, if the chosen number is 4827 and the player
guesses 4273, the computer would respond with "1 bull, 2 cows" (1-2),
because the player guessed one digit that is in the correct position
(4), and two digits that are in the chosen number, but in a different
position (2, 7).
7. The player continues to guess until they correctly guess the entire
number (i.e., four bulls).''' + RESET_ALL)
    print(ERR_COLOR + 'Your challenge: ', end='' + RESET_ALL)
    print('try to guess the number ', end='')
    print('in no more than 7 attempts.' + RESET_ALL)
    print(
        ILINE_COLOR +
        '''-------------------------------------------------------------------
The computer has just generated a number that you need to guess.
Give it a try!
-------------------------------------------------------------------'''
        + RESET_ALL)


game_rules()


def number_generator():
    '''
    Generates 4-digit number (list of 4 random unique digits)
    '''
    generated_number = []
    while len(generated_number) < 4:
        element = randint(0, 9)
        if element not in generated_number:
            generated_number.append(element)
    return generated_number


secret_number = number_generator()

if DEBUG:
    print(secret_number)


class Guess:
    '''
    Main Guess class. The class takes two lists as parameters during
    initialization. The first parameter is passed as an argument when
    creating an instance of the class, which is based on user input.
    The second parameter contains a list of digits for the secret number.
    The class also contains an attribute called guess_list, which adds
    to the list instance attributes after each initialization
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
        Generates a dictionary of guess/score pairs as key|value pairs and
        prints all scores in the terminal in user-friendly format
        '''
        all_scores = {}
        for i in Guess.guess_list:
            guess_string = ''.join(str(num) for num in i.my_guess)
            all_scores[guess_string] = [i.bull_counter(), i.cow_counter()]
            guess_str = "-".join(str(num) for num in i.my_guess)
            score_list = [i.bull_counter(), i.cow_counter()]
            score_str = "-".join(str(num) for num in score_list)
            print(f"{guess_str} | {score_str}")
        return all_scores


# this variable is used to keep track of all the user's guesses
# that have been made so far, and it is updated every time a new
# Guess object is created
guess_list = []


def get_guess():
    '''
    Receives guess number from the User. Creates class Guess instances.
    The loop will repeatedly request data, until it is valid
    '''
    while True:
        guess_string = input(
            MAKE_GUESS +
            '''Please make your guess, input your four unique-digit number:
-------------------------------------------------------------------\n'''
            + RESET_ALL)
        if validate_guess(guess_string):
            break
    # converting user input (numerical string) into a list of numbers
    users_guess = [int(num) for num in list(guess_string)]
    # creates an instance og main class Guess
    guess = Guess(users_guess, secret_number)
    guess_list.append(guess_string)
    return guess


def validate_guess(values):
    '''
    Contains five exception to validate user input.
    '''
    try:
        if len([i for i in values if not i.isdigit()]) > 0:
            unacceptable_chars = [i for i in values if not i.isdigit()]
            error_msg = (
                f'input contains unacceptable character(s): '
                f'{VARIABLE_COLOR}{", ".join(unacceptable_chars)}{RESET_ALL}'
            )
            raise ValueError(error_msg)
    except ValueError as err:
        print(f'''Invalid data: {ERR_COLOR}{err}{RESET_ALL}.
Try again.''')
        return False

    try:
        if len(values) != 4 and len(values) != 0:
            raise ValueError(
                            f"exactly 4 values required, you provided "
                            f"{VARIABLE_COLOR}{len(values)}{RESET_ALL}")
    except ValueError as err:
        print(f'''Invalid data: {ERR_COLOR}{err}{RESET_ALL}.
Try again.''')
        return False

    try:
        if len(values) == 0:
            raise ValueError('you should not leave an empty field')
    except ValueError as err:
        print(f'''Invalid data: {ERR_COLOR}{err}{RESET_ALL}.
Try again.''')
        return False

    try:
        if values in list(guess_list):
            raise ValueError(f'you have already made this guess: '
                             f'{VARIABLE_COLOR}{values}{RESET_ALL}')
    except ValueError as err:
        print(f'''Invalid data: {ERR_COLOR}{err}{RESET_ALL}.
Try again.''')
        return False

    try:
        if len(values) != len(set(values)):
            repeated_digits = {i for i in values if values.count(i) > 1}
            repeated_digits_str = ' and '.join(str(x) for x in repeated_digits)
            error_msg = (
                        f"you have repetitive digit(s) in your guess: "
                        f"{VARIABLE_COLOR}{repeated_digits_str}{RESET_ALL}"
            )
            raise ValueError(error_msg)
    except ValueError as err:
        print(f'''Invalid data: {ERR_COLOR}{err}{RESET_ALL}.
Try again.''')
        return False

    return True


def restart_game():
    '''
    Resets game data after each game cycle
    '''
    global secret_number, guess_list
    secret_number = number_generator()
    guess_list = []
    Guess.guess_list = []
    print(
                RULES_COLOR +
                '''
Game restarted. New secret number was successfully generated!
-------------------------------------------------------------------'''
                + RESET_ALL)


def main():
    '''
    Calls the get_guess function until the right User's guess. Then, depending
    on the user's choice, it either restarts the game or exits it
    '''
    while True:
        guess = get_guess()
        guess.show_all_scores()
        if guess.bull_counter() == 4:
            break
    print()
    print(WIN_BCOLOR + 'Congratulations! You win!!!' + RESET_ALL)
    print('''-------------------------------------------------------------------
Input Y if you want to play again. To quit the game input N.
Input field supports upper and lower case.
-------------------------------------------------------------------''')
    while True:
        users_choice = input()
        if users_choice.lower() == 'y':
            restart_game()

            if DEBUG:
                print(secret_number)

            main()
            return False
        if users_choice.lower() == 'n':
            print(
                RULES_COLOR +
                '''
Thank you for playing Bulls and Cows game. Hope to see you soon!
-------------------------------------------------------------------'''
                + RESET_ALL)

            print(
                DIM +
                'To play again, click on the "RUN PROGRAM" button.'
                + RESET_ALL)

            return False
        print(
            ERR_COLOR +
            f"Invalid input {VARIABLE_COLOR}{users_choice}{RESET_ALL}. " +
            ERR_COLOR +
            "Please input Y or N to confirm your choice\n" +
            "Input field supports upper and lower case." +
            ERR_COLOR + '''
-------------------------------------------------------------------'''
            + RESET_ALL)


main()
