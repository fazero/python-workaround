__author__ = 'fazero'

# Auxiliary tools

from functools import update_wrapper
import time
import cProfile

def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result

# Main section

@memo
def freq_seq(n):
    seq = ""
    if n == 1: seq = "1"
    if n > 1: seq = "11"
    if n > 2:
        for i in range(2, n):
            newseq = ""
            count = 1
            for j in range(1, len(seq)):
                if seq[j] == seq[j-1]:
                    count += 1
                    continue
                else:
                    newseq += str(count) + seq[j-1]
                    count = 1
            seq = newseq + str(count) + seq[-1]
    return seq

for i in range(50):
    print "i =", i, "\t\tsequence is \"%s\"" % freq_seq(i)