"Question 1: Two Sum"
"""Problem:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.
    Assume there is exactly one solution.
    Do not use the same element twice.
    Return answer in any order."""

""" Example:
Input: nums = [1, 2, 7, 11, 15], target = 9  
Output: [1,2]  (because nums[1] + nums[2] = 2 + 7 = 9)"""

import unittest

def two_sum(nums, target):
    lookup = {}  # stores number -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return None

class Test_two_sum(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_with_negatives(self):
        self.assertEqual(two_sum([-3, 4, 3, 90], 0), [0, 2])

    def test_multiple_solutions(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_with_zeros(self):
        self.assertEqual(two_sum([0, 4, 3, 0], 0), [0, 3])

    def test_large_case(self):
        self.assertEqual(two_sum([1, 5, -2, 7, 10], 8), [0, 3])

if __name__ == '__main__':
    unittest.main()
