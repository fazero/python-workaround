import time

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result

# --------------
# User Instructions
#
# Write a function, compile_word(word), that compiles a word
# of UPPERCASE letters as numeric digits. For example:
# compile_word('YOU') => '(1*U + 10*O +100*Y)' 
# Non-uppercase words should remain unchaged.

def compile_word_1(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if ord(word[0]) >= ord('A') and ord(word[0]) <= ord('Z'):
        length = len(word)
        result = '('
        for i in range(length - 1):
            position = length - i - 1
            result += '1' + '0' * i + '*' + word[position] + '+'
        result += '1' + '0' * (length - 1) + '*' + word[0] + ')'
        return result
    return word

def compile_word_2(word):
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
               for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    return word


def test(f, n):
    for i in xrange(n):
        assert f('MESSIR') == '(1*R+10*I+100*S+1000*S+10000*E+100000*M)'
        assert f('YOU') == '(1*U+10*O+100*Y)'
        assert f('you') == 'you'
    return 'Function "' + f.__name__ + '" passed.'

print timedcall(test, compile_word_1, 100000)
print timedcall(test, compile_word_2, 100000)
