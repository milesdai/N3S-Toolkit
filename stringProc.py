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

def strip_aux(s):
    return ''.join(c for c in s if c in string.ascii_letters or c in string.digits)

def filter_str(s, letters_to_remove):
    # letters_to_remove should be a string of letters to be filtered out
    return ''.join(c for c in s if c not in letters_to_remove)

# Reg-Ex
# https://docs.python.org/3.5/library/re.html
def re_match(s, pattern):
    p = re.compile(pattern)
    return p.match(s) is not None

def re_filter(str_list, pattern):
    p = re.compile(pattern)
    return [s for s in str_list if p.match(s) is not None]