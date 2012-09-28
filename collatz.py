#Collatz Returns!


#Define a procedure, collatz_steps, that takes as input a positive integer, n, and returns
#the number of steps it takes to reach 1 by following these steps:

#    If n is even, divide it by 2. (You can test for evenness using n % 2 == 0.)
#    If n is odd, replace it with 3n + 1.

def collatz__steps(number):
    steps = 0
    if number < 1:
        return 'Error: the number is out of range'
    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        steps = steps + 1
    return steps


def collatz_steps(number):
    if number < 1:
        return 'Error: the number is out of range'
    elif number == 1:
        return 0
    elif number % 2 == 0:
        return 1 + collatz_steps(number / 2)
    else:
        return 1 + collatz_steps(3 * number + 1)
#For example,

print collatz_steps(1)
#>>> 0

print collatz_steps(2)
#>>> 1

print collatz_steps(6)
#>>> 8

print collatz_steps(101)
#>>> 25
