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

    print(list_num)
    return list_num


secret_number = number_generator()


def bull_counter(list1, list2):
    '''
    Counts the number of digits that are in the correct position
    '''
    bull_counter = 0
    for i in range(4):
        if list1[i] == list2[i]:
            bull_counter += 1
    return bull_counter

result_1 = bull_counter([1,2,3,4], [1,2,3,4])
print(result_1)


def cow_counter(list1, list2):


