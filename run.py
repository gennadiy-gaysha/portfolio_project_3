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

# nano ~/.bashrc
# alias rr='python3 run.py'
# source ~/.bashrc


def number_generator():
    '''
    Function generats 4-digit number (list of 4 random unique digits) 
    '''
    list_num = []
    while len(list_num) < 4:
        a = randint(0, 9)
        if a not in list_num:
            list_num.append(a)

    return list_num


secret_number = number_generator()


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

    def __init__(self, my_guess, secret=secret_number):
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
            if (self.my_guess[i] in self.secret) and (self.my_guess[i] != self.secret[i]):
                cow_counter += 1
        return cow_counter

    def show_all_scores(self):
        for i in Guess.guess_list:
            print(i.my_guess)


guess1 = Guess([2, 4, 5, 6])
guess2 = Guess([2, 7, 5, 0])
guess3 = Guess([1, 9, 3, 6])
# BULL1 = guess1.bull_counter()
# COW1 = guess1.cow_counter()
# print(secret_number)
# print(f'{guess1.my_guess}|{BULL1}-{COW1}')
guess3.show_all_scores()








