# adventofcode19

Solutions to [adventofcode 2019](https://adventofcode.com/) in python.

## Running solutions for day dd

~~~sh
python3 solutions/solution_dd.py 1 input/dd.txt
python3 solutions/solution_dd.py 2 input/dd.txt
~~~

## Running tests for day dd

For the tests using the input it is actually important to run the tests from the repository directory.

~~~sh
python3 -m doctest -v solutions/solution_dd.py
~~~

## Lessons Learned

- 01.12.
  - First time using doctests.
- 02.12.
  - Remember: itertools.product is the Replacement for n for loops.
  - Remember: l=l2.copy() to make a shallow copy
