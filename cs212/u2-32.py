# -------------
# User Instructions
#
# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????. 

import string, re, itertools, time, cProfile

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result


examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BD**2 == CE**2""".splitlines()


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = "".join([l for l in 'ABCDEFGHIJKLMNOPQRSTUVW' if l in formula]) #should be a string
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    """Formula f is valid if and only if it has no 
    numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


def test():
    t0 = time.clock()
    for example in examples:
        print;
        print 13 * ' ', example
        print '%6.4f sec.   %s ' % timedcall(solve, example)
    print '%6.4f tot.' % (time.clock() - t0)

import cProfile
cProfile.run('test()')
