"""illustration of two codes doing same task, but with different time efficiency"""


def print_even():
    number = 2
    while number <= 100:
        if number % 2 == 0:
            print(number)
        number += 1


print_even()


"""second illustration of the same code but with different approach"""

print("---------------------------------second example------------------------------------------")

def print_even():
    number = 2
    while number <= 100:
        print(number)
        number += 2


print_even()

"""which code runs faster ??"""

"""
the second one right ??
because the first one loop has to go over a 100 times before completion
but the second code loop has to go over a 50 times to complete execution
so now we say in terms of time efficiency the second code is more efficient
than the first code.
"""
