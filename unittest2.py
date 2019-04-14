#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 02:22:12 2019

@author: abhijithneilabraham
"""

import unittest
class Test_unit(unittest.TestCase):
     def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)
if __name__=="__main__":
    unittest.main()
    