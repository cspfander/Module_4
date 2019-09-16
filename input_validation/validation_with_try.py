"""
Program: validation_with_try.py
Author: Colten Pfander
Last date modified: 9/16/2019



The purpose of this program is to read in one person's names (first and last), age, and three scores out of 100.
Then it is to take the three scores, find the average, and store it into a variable with input validation.
"""


def average(test_1, test_2, test_3):
    if int(test_1) < 0:
        raise ValueError
    else:
        average_score = (int(test_1) + int(test_2) + int(test_3)) / 3
        return float(average_score)


if __name__ == '__main__':
    last_name = input('Please enter your last name: ')
    first_name = input('Please enter your first name: ')
    age = input('Please enter your age: ')

    average_scores = average(85, 90, 95)

    print(last_name + ', ' + first_name + ' age: ' + age + ' grade: ' + str(average_scores))
    # inputs:
    # Please enter your last name: Pfander
    # Please enter your first name: Colten
    # Please enter your age: 23
    # Please enter the score for test 1: 92
    # Please enter the score for test 2: 91
    # Please enter the score for test 3: 97
    # output:
    # Pfander, Colten age: 23 grade: 93.33
