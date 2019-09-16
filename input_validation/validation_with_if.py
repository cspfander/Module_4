"""
Program: average_scores.py
Author: Colten Pfander
Last date modified: 9/8/2019



The purpose of this program is to read in one person's names (first and last), age, and three scores out of 100.
Then it is to take the three scores, find the average, and store it into a variable.
"""


def average():
    # Get input for scores
    test_1 = input('Please enter the score for test 1: ')
    test_2 = input('Please enter the score for test 2: ')
    test_3 = input('Please enter the score for test 3: ')
    return (int(test_1) + int(test_2) + int(test_3)) / 3  # calculation using score1, score2, and score 3


if __name__ == '__main__':
    last_name = input('Please enter your last name: ')
    first_name = input('Please enter your first name: ')
    age = input('Please enter your age: ')

    average_scores = average()

    print(last_name + ', ' + first_name + ' age: ' + age + ' grade: {0:.2f}' .format(average_scores))
    # inputs:
    # Please enter your last name: Pfander
    # Please enter your first name: Colten
    # Please enter your age: 23
    # Please enter the score for test 1: 92
    # Please enter the score for test 2: 91
    # Please enter the score for test 3: 97
    # output:
    # Pfander, Colten age: 23 grade: 93.33
