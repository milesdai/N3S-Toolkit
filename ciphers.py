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
    pass 

if __name__ == "__main__":
    import doctest
    doctest.testmod()