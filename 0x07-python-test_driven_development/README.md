# 0x07. Python - Test-driven development
## :open_book: Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
 * Why Python programming is awesome
 * What’s an interactive test
 * Why tests are important
 * How to write Docstrings to create tests
 * How to write documentation for each module and function
 * What are the basic option flags to create tests
 * How to find edge cases
## Requirements
### Python Test Cases
* Allowed editors: `vi`, `vim`, `emacs`
* All your files should end with a new line
* All your test files should be inside a folder `tests`
* All your test files should be text files (extension: `.txt`)
* All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
* All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)')`
* All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)')`
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!
## Tasks
### 0. Integers addition
Write a function that adds 2 integers.
 * Prototype: `def add_integer(a, b=98):`
### 1. Divide a matrix
Write a function that divides all elements of a matrix.
 * Prototype: `def matrix_divided(matrix, div):`
### 2. Say my name
Write a function that prints `My name is <first name> <last name>`
 * Prototype: `def say_my_name(first_name, last_name=""):`
### 3. Print square
Write a function that prints a square with the character `#`.
 * Prototype: `def print_square(size):`
### 4. Text indentation
Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`
 * Prototype: `def text_indentation(text):`
### 5. Max integer - Unittest
Since the beginning you have been creating “Interactive tests”. For this exercise, you will add Unittests.
In this task, you will write unittests for the function `def max_integer(list=[]):.`
