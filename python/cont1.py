#!/usr/bin/env python

def generate_hapiness(good, bad):
    def hpns(x):
        if x in good:
            return 1
        elif x in bad:
            return -1
        else:
            return 0
    return hpns

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    S = map(int, input().strip().split())
    A = set(map(int, input().strip().split()))
    B = set(map(int, input().strip().split()))
    hapiness = generate_hapiness(good=A, bad=B)
    print(sum(hapiness(x) for x in S))