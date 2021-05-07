#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program lets the user guess a number between 1-10
#   with a randomized integer and tells them if they are
#       correct or not


import random


def main():
    # this function lets the user pick a number between 1-10
    #   and randomizes said number

    # input
    guess = input("Guess an integer between 1-10: ")
    randomized_number = random.randint(1, 10)  # a number between 1-10

    # process & output
    try:
        guess_int = int(guess)

        if guess_int > 10:
            print("\nYou have entered an integer that is too large!")
            print("Answer was {0}".format(randomized_number))

        elif guess_int < 1:
            print("\nYou have entered an integer that is too small!")
            print("Number was {0}".format(randomized_number))

        elif guess_int == randomized_number:
            print("\nYou are correct")

        elif guess_int != randomized_number:
            print("\nYou are not correct, the answer was {0}"
                  .format(randomized_number))

    except Exception:
        print("\nYou have not entered an integer.")
        print("Number was {0}".format(randomized_number))

    finally:
        print("\nThank you for playing!")


if __name__ == "__main__":
    main()
