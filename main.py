"""illustration of two codes doing same task, but with different time efficiency"""


def print_even():
    number = 2
    while number <= 100:
        if number % 2 == 0:
            print(number)
        number += 1


print_even()


"""second illustration of the same code but with different approach"""


def print_even():
    number = 2
    while number <= 100:
        print(number)
        number += 2


print_even()

