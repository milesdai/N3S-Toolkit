import string

def caesar(text, shift):
    """
    Shifts text by shift

    Preserves case, spacing, and symbols.    
    >>> caesar('abc', 1)
    'bcd'
    >>> caesar('ABc', 2)
    'CDe'
    >>> caesar('aB:=- *c', 27)
    'bC:=- *d'
    """
    res = ''
    for s in text:
        if s.isupper():
            res += chr((ord(s) + shift - 65) % 26 + 65)
        elif s.islower():
            res += chr((ord(s) + shift - 97) % 26 + 97)
        else:
            res += s
    return res

def atbash(text):
    """
    Applies the atbash transformation on text.

    >>> atbash('abc')
    'zyx'
    >>> atbash('AbC')
    'ZyX'
    >>> atbash('A1b!xZ')
    'Z1y!cA'
    """
    res = ''
    for s in text:
        if s.isupper():
            res += string.ascii_uppercase[25 - string.ascii_uppercase.index(s)]
        elif s.islower():
            res += string.ascii_lowercase[25 - string.ascii_lowercase.index(s)]
        else:
            res += s 
    return res

if __name__ == "__main__":
    import doctest
    doctest.testmod()