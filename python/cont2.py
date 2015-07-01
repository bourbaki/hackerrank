#!/usr/bin/env python

from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)
        
if __name__ == '__main__':
    n = int(input())
    vals = OrderedCounter(input().strip() for _ in range(n)).values()
    print(len(vals))
    print(*vals)