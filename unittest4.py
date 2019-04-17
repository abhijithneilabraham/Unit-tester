#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 21:21:37 2019

@author: abhijithneilabraham
"""

import unittest
class testingmethods(unittest.TestCase):
    def test1(self):
        try:
            self.assertEqual('foo'.upper(),'FOo')
        except AssertionError:
            print('The string is not uppercase')
            
        
    def test2(self):
        self.assertEqual('foo'.upper(),'FOO')
    
tester=testingmethods()
tester.test1()



