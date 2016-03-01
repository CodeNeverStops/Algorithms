#!/usr/bin/python
# -*- coding: utf-8 -*-

def dfs_map(x, y, step):
    global min_step
    direction = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
            )
    if x == target[0] and y == target[1]: # reach the target
        if step < min_step:
            min_step = step
        return

    for d in direction:
        tx = x + d[0] # target x
        ty = y + d[1]
        if tx < 0 or tx > (map_row_len - 1) or ty < 0 or ty > (map_col_len - 1):
            continue
        if map1[tx][ty] == 0 and book[tx][ty] == 0:
            book[tx][ty] = 1
            dfs_map(tx, ty, step + 1)
            book[tx][ty] = 0


if __name__ == '__main__':
    min_step = 9999
    start = (0, 0)
    target = (3, 2)
    map1 = (
            (0, 0, 1, 0), # 1 means wall
            (0, 0, 0, 0),
            (0, 0, 1, 0),
            (0, 1, 0, 0),
            (0, 0, 0, 1)
            )
    map_row_len = len(map1)
    map_col_len = len(map1[0])
    book = [[0 for col in range(map_col_len)] for row in range(map_row_len)]
    book[start[0]][start[1]] = 1
    dfs_map(start[0], start[1], 0)
    print 'min step:', min_step
