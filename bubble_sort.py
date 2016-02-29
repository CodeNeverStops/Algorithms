#!/usr/bin/python
# -*- coding: utf-8 -*-

def bubble_sort(numbers):
    nums = numbers
    count = len(nums)
    for i in range(1, count):
        for j in range(0, count - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

if __name__ == '__main__':
    list1 = [1, 3, 2, 1, 4, 0, 1.5, -0.1]
    ret = bubble_sort(list1)
    print ret

