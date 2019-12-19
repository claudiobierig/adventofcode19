#!/usr/bin/env python

import math

def read_input(path):
    with open(path) as file:
        return [int(c) for c in file.readline().strip()]

def get_pattern(offset, n):
    """
    >>> get_pattern(0, 1)
    0
    >>> get_pattern(1, 1)
    0
    >>> get_pattern(2, 1)
    1
    >>> get_pattern(3, 1)
    1
    >>> get_pattern(4, 1)
    0
    >>> get_pattern(5, 1)
    0
    >>> get_pattern(6, 1)
    -1
    >>> get_pattern(7, 1)
    -1
    >>> get_pattern(8, 1)
    0
    """
    position = int(offset/(n+1))%4
    if position == 0:
        return 0
    elif position == 1:
        return 1
    elif position == 2:
        return 0
    elif position == 3:
        return -1
    
def transform(sequence):
    """
    >>> sequence = [int(c) for c in "12345678"]
    >>> transform(sequence)
    [4, 8, 2, 2, 6, 1, 5, 8]
    """
    return [abs(n)%10 for n in get_sum(sequence, 1)]


def get_offset(sequence):
    offset = 0
    for i in range(7):
        offset += sequence[i]*pow(10, 6-i)
    return offset

def transform2(sequence, offset):
    for j in range(len(sequence)-2,offset-1,-1):
        sequence[j] = (sequence[j] + sequence[j+1])%10

def get_sum(sequence, offset):
    result = [0]*len(sequence)
    for n in range(len(sequence)):
        for i, x in enumerate(sequence):
            result[n] += x*get_pattern(i+offset,n)
        
    return result

def get_output(digit_list):
    """
    >>> get_output([1,2,3])
    '123'
    """
    return ''.join([str(i) for i in digit_list])

if __name__ == "__main__":
    sequence = read_input("input/16.txt")
    for _ in range(100):
        sequence = transform(sequence)

    print("Solution 1")
    print(get_output(sequence[0:8]))

    sequence = read_input("input/16.txt")
    sequence = sequence*10000
    offset = get_offset(sequence)
    assert(offset>=(len(sequence)/2))
    for _ in range(100):
        transform2(sequence, offset)
    
    print(get_output(sequence[offset:offset+8]))
