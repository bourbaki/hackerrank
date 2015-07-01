#!/usr/bin/env python

def fibonacci_generator(n):
    """generates n fibonacci numbers"""
    a, b = 1, 0
    for i in range(n):
        if i == 0:
            yield b
        elif i == 1:
            yield a
        else:
            a, b = a + b, a
            yield a

if __name__ == '__main__':
    n = int(input())
    print([i ** 3 for i in fibonacci_generator(n)])