"Question 1: Reverse String "
"""Problem:
    Write a function that reverses a string.
    Input string is given as a character array s.
    You must do it in-place with O(1) extra memory."""

""" Example:
Input: s = ["h","e","l","l","o"]  
Output: ["o","l","l","e","h"]"""

import unittest

def reverse_my_string(name_list):
    #space complexity : O(1)
    left , right = 0 , len(name_list)-1
    while left < right:
        name_list[left] , name_list[right] = name_list[right] , name_list[left]
        left += 1
        right -= 1
    return name_list

    #traditional approach: this will increase space
    # length = len(name_list)
    # reversed_list = []
    # for i in range(length):
    #     reversed_list.append(name_list[length - 1 - i])
    # return reversed_list

class Test(unittest.TestCase):
    def test_basic_word(self):
        s = ["h", "e", "l", "l", "o"]
        reverse_my_string(s)
        self.assertEqual(s, ["o", "l", "l", "e", "h"])

    def test_even_length_word(self):
        s = ["a", "b", "c", "d"]
        reverse_my_string(s)
        self.assertEqual(s, ["d", "c", "b", "a"])

    def test_single_character(self):
        s = ["x"]
        reverse_my_string(s)
        self.assertEqual(s, ["x"])

    def test_empty_list(self):
        s = []
        reverse_my_string(s)
        self.assertEqual(s, [])

    def test_palindrome(self):
        s = ["r", "a", "c", "e", "c", "a", "r"]
        reverse_my_string(s)
        self.assertEqual(s, ["r", "a", "c", "e", "c", "a", "r"])

if __name__ == '__main__':
    unittest.main()