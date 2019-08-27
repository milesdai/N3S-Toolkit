import string
import re

def get_upper():
    return string.ascii_uppercase

def get_lower():
    return string.ascii_lowercase

def to_upper(s):
    return s.upper()

def to_lower(s):
    return s.lower()

def reverse(s):
    return s[::-1]

def strip_aux(s):
    return ''.join(c for c in s if c in string.ascii_letters or c in string.digits)

def filter_str(s, letters_to_remove):
    # letters_to_remove should be a string of letters to be filtered out
    return ''.join(c for c in s if c not in letters_to_remove)

def index_to_letter(n, lowercase=True):
    """
    Returns the 1-indexed letter corresponding to the index n

    >>> index_to_letter(2)
    'b'
    >>> index_to_letter(27, lowercase=False)
    'A'
    """
    assert n > 0
    if lowercase:
        return string.ascii_lowercase[(n - 1) % 26]
    else:
        return string.ascii_uppercase[(n - 1) % 26]
    
def indices_to_letters(indices, lowercase=True):
    """
    Returns the 1-indexed letter corresponding to the index n

    >>> indices_to_letters([1,2,3])
    'abc'
    >>> indices_to_letters([27, 28, 29], lowercase=False)
    'ABC'
    """
    result = ''
    for i in indices:
        result += index_to_letter(i, lowercase)
    return result 

def index_into(string, index):
    """
    Returns the character at the 1-indexed position in string

    >>> index_into('puzzle', 3)
    'z'
    """
    if index > len(string) or index < 1:
        raise ValueError('Index {} does not fit into the string {}. Remember that index should be 1-indexed.'.format(index, string))
    return string[index - 1]

def is_palindrome(s):
    """
    Returns true if the input (number or string) is a palindrome.

    >>> is_palindrome('abcba')
    True
    >>> is_palindrome(1234321)
    True
    >>> is_palindrome('ab12')
    False
    """
    return str(s) == str(s)[::-1]

# Reg-Ex
# https://docs.python.org/3.5/library/re.html
def re_match(s, pattern):
    p = re.compile(pattern)
    return p.match(s) is not None

def re_filter(str_list, pattern):
    p = re.compile(pattern)
    return [s for s in str_list if p.match(s) is not None]

if __name__ == "__main__":
    import doctest
    doctest.testmod()