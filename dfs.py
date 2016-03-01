#!/usr/bin/python
# -*- coding: utf-8 -*-

def dfs(step, n, book, pool):
    '''Depth First Search'''
    if step == n:
        print pool
        return

    for i in range(n):
        if book[i]: # is used
            continue
        pool[step] = i + 1
        book[i] = 1 # mark as used
        dfs(step + 1, n, book, pool)
        book[i] = 0 # mark as unused

    return

if __name__ == '__main__':
    n = 4
    # record used status
    book = [0] * n
    # a pool to store result
    pool = [0] * n
    dfs(0, n, book, pool)
