import datetime
import random

DIGITS = 4

def start_bulls_cows():
    print("Hi there!")
    print("--------------------------")
    generated_number = generate_number()
    print("I've generated a random 4 digit number for you. Let's play a bulls and cows game.")
    print("--------------------------")
    print("Enter a number:")
    print("--------------------------")
    guesses = 0
    start_time = datetime.datetime.now()
    while True:
        user_input = input(">>> ")
        if not is_user_input_valid(user_input):
            continue
        guesses += 1
        if check_number(str(generated_number), user_input):
            break
    end_time = datetime.datetime.now()
    print("Correct, you've guessed the right number in " + str(guesses) + " guesses!")
    print("--------------------------")
    print_result(guesses)
    print("Total time was " + str(end_time - start_time))
    print("--------------------------")


def generate_number():
    generated_number = random.randint(1, 9)
    digit_position = 1
    while digit_position < DIGITS:
        random_digit = random.randint(0, 9)
        if str(random_digit) not in str(generated_number):
            generated_number *= 10
            generated_number += random_digit
            digit_position += 1
    return generated_number


def is_user_input_valid(user_input):
    if not user_input.isnumeric() or len(user_input) != DIGITS:
        print("Input is not number or 4 digits length")
        return False
    elif user_input[0] == "0":
        print("Input cannot start with 0")
        return False
    elif len(user_input) != len(set(user_input)):
        print("Input contains duplicities")
        return False
    return True


def check_number(generated_number, user_number):
    bulls_count = 0
    cows_count = 0
    for generated_index in range(len(generated_number)):
        if generated_number[generated_index] == user_number[generated_index]:
            bulls_count += 1
            continue
        for user_index in range(len(user_number)):
            if generated_index != user_index and generated_number[generated_index] == user_number[user_index]:
                cows_count += 1
                break
    print(str(bulls_count) + " " + add_suffix_if_needed("bull", bulls_count) + ", "
          + str(cows_count) + " " + add_suffix_if_needed("cow", cows_count))
    print("--------------------------")
    return bulls_count == 4


def add_suffix_if_needed(text, number):
    if number == 1:
        return text
    return text + "s"


def print_result(guesses):
    if guesses < 8:
        result = "amazing"
    elif guesses < 18:
        result = "average"
    elif guesses < 30:
        result = "not so good"
    else:
        result = "bad"
    print("That's " + result + " result")


start_bulls_cows()
