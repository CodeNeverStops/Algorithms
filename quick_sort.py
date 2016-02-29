#!/usr/bin/python
# -*- coding: utf-8 -*-
def quick_sort(nums, left, right):
    if left > right:
        return

    base = nums[left] # baseline
    i = left # left guard
    j = right # right guard

    while i != j:

        while nums[j] >= base and j > i: # go to left until nums[j] < base
            j -= 1

        while nums[i] <= base and i < j: # go to right until nums[i] > base
            i += 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    # exchange nums[left] and nums[i] when i == j
    nums[left], nums[i] = nums[i], base

    quick_sort(nums, left, i - 1)
    quick_sort(nums, i + 1, right)


if __name__ == '__main__':
    list1 = [1, 3, 2, 4, 1, 0, 1.5, -0.1]
    quick_sort(list1, 0, len(list1) - 1)
    print list1
