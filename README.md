# N3S Toolkit
## About
The goal of this project is to create easy-to-access scripts for use during puzzle hunts. Ideally, these scripts should be accessible to people who may not be as fluent in CS or Python. As a result, some scripts are simply wrappers for existing Python functions albeit maybe in a more logical organization or a more readable name. If there's a tradeoff, prioritize speed and ease-of-use over speed of execution.

## Installation
Run the installation script with Python3:
```
python3 setup.py install --record installed_files.txt
```
If that doesn't work, make sure you have Python 3 installed and run the command above with ```python```. 

The ```installed_files.txt``` file shows paths to all the installed files. Simply delete these files to uninstall the package. Alternatively, ```pip3``` should be able to find most of the installed files, so you can uninstall with ```pip3 uninstall n3s_toolkit``` if you don't mind leaving a few small files behind.

## Usage
After installing, you can import the n3s_toolkit package
```py
>>> import n3s_toolkit as nt
>>> nt.ciphers.caesar('abc', 3)
'def'
```
To avoid typing n3 and use the modules directly, import the entire  ```n3s_toolkit``` package.
```py
>>> from n3s_toolkit import *
>>> ciphers.caesar('abc', 3)
'def'
```
For more fine-grained control over imports:
```py
>>> from n3s_toolkit import ciphers
>>> ciphers.caesar('abc', 3)
'def'
```

## Contributing
Check TODO.md for ideas of things to add.

The source code is located inside the n3s_toolkit directory. If you create a new module (i.e. a new .py file) under n3s_toolkit, make sure to add it to ```__init__.py``` under the ```__all__``` list and the list of imports to ensure that it gets imported with the ```import *``` operator.

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

