# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '': return (0, 0)
    text_len = len(text)
    sps = []
    for i in range(text_len - 1):
        if i < text_len - 1:
            j1, j2 = i, i + 1
            if (text[j1].upper() == text[j2].upper()):
                while (text[j1].upper() == text[j2].upper() and j1 > 0 and j2 < (text_len - 1)):
                    j1, j2 = j1 - 1, j2 + 1
                sps.append((j1, j2 + 1))
        if i < text_len - 2:
            j1, j2 = i, i + 2
            if (text[j1].upper() == text[j2].upper()):
                while (text[j1].upper() == text[j2].upper() and j1 > 0 and j2 < (text_len - 1)):
                    j1, j2 = j1 - 1, j2 + 1
                if j1 <= 0 or  j2 >= (text_len - 1): sps.append((j1, j2 + 1))
                else: sps.append((j1 + 1, j2))
        sps.append((i, i + 1))
    return max(sps, key=lambda (x, y): y - x)


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('asdRacecar') == (3, 10)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print longest_subpalindrome_slice('asdRacecar')
print test()