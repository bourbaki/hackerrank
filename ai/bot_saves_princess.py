#!/usr/bin/env python

import operator

def displayPathtoPrincess(grid):
    coords = {c: (i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == 'm' or c == 'p'}
    return dist2steps(dist(coords['p'], coords['m']))

def dist(p1, p2):
    return tuple(map(operator.sub, p1, p2))
    
def dist2steps(d):
    steps = []
    steps.extend(["DOWN" if d[0] > 0 else "UP"] * abs(d[0]))
    steps.extend(["RIGHT" if d[1] > 0 else "LEFT"] * abs(d[1]))
    return steps
        
if __name__ == '__main__':
    m = int(input())
    grid = []
    for i in range(0, m): 
        grid.append(input().strip())
    for step in displayPathtoPrincess(grid):
        print(step)