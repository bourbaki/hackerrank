#!/usr/bin/env python

from collections import deque

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        _ = input()
        line = list(map(int, input().strip().split()))
        increasing = False
        ret_str = "Yes"
        for i in range(len(line)-1):
            if not increasing and line[i] < line[i+1]:
                increasing = True
            elif increasing and line[i] > line[i+1]:
                ret_str = "No"
                break
        print(ret_str)
    