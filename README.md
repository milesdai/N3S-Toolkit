# N3S Toolkit
## About
The goal of this project is to create easy-to-access scripts for use during puzzle hunts. Ideally, these scripts should be accessible to people who may not be as fluent in CS or Python. As a result, some scripts are simply wrappers for existing Python functions albeit maybe in a more logical organization or a more readable name. If there's a tradeoff, prioritize speed and ease-of-use over speed of execution.

## Usage
In a puzzlehunt scenario, open a terminal window or .py file in the toolkit directory and simply import the functions you wish to use. For example, to use the caesar cipher function:
```python
# Import the whole package
import ciphers
print(ciphers.caesar('abcd', 4))

# Or import the function by name
from ciphers import caesar
print(caesar('abcd', 4))
```
In the future, we may convert this into a formal Python package, but for now, it's just a collection of scripts.

## Testing
This project uses doctests to run lightweight sanity-check tests on the functions you write. Doctests are placed in the docstrings of each function and are formated like interactive Python sessions. Type the test command after the ```>>>``` and the expected result on the next line. The following example shows how to use doctests for a sample method, square, which returns the square of a number.
```python
def square(n):
    """
    Returns the square of a number.

    >>> square(2)
    4
    >>> square(-5)
    25
    >>> [square(n) for n in range(4)]
    [0, 1, 4, 9]
    """

    return n**2

if __name__ == "__main__":
    import doctests
    doctest.testmod()
```
Assuming the function is written in a file called ```square.py```, run the tests by calling ```python square.py```. Nothing should show up unless a test errors out. Use the ```-v``` flag to force the tests to print: ```python square.py -v```.

For more information, see the [documentation](https://docs.python.org/3/library/doctest.html).

## Functions to Add
* Dictionaries
    * American English
    * British English
    * proper nouns
* String Modification
    * String filtering (removing auxillary chars)
    * Permutations (i.e. anagrams)
    * indexing into strings
    * reversing a string
    * transpose distance
* Ciphers
    * Morse code
    * ~~Caesar Ciphers~~
    * ~~Atbash~~
    * Pigpen
    * Semaphores?
* Image processing
* Audio processing
* Geometry
    * Tesselation solvers
    * Graph solvers
