def simple(n):
    """This is a docstring...
This is a second docstring...
    """
    for x in xrange(2, n):
        if n % x == 0: return 0
    return 1

simples = filter(simple, xrange(2, 4000))

def sum(seq):
    def add(x, y): return x + y
    return reduce(add, seq, 0)

print sum(xrange(1, 983))
print sum([])

x, y = 1, (2, 4)
