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
python3 -m doctest -v solutions/*.py
python3 solutions/test_*.py -v
~~~

## Lessons Learned

- 01.12.
  - First time using doctests.
- 02.12.
  - Remember: itertools.product is the Replacement for n for loops.
  - Remember: l=l2.copy() to make a shallow copy
- 06.12.
  - Remember: x = lambda input : output
  - For larger tests doctest is not the right choice. Need to restructure for the next intcomputer
  - For the next graph puzzle I'll try [NetworkX](https://networkx.github.io/documentation/stable/index.html) instead of just using a dict.
  - Remember: python3: d.items(), python2: d.iteritems()
- 07.12.
  - itertools.permutations gives all possible permutations
  - generators for input where not the best choice
