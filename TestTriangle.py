# -*- coding: utf-8 -*-
"""
Updated Sept 7, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author: Nicole Hilden
"""

import unittest

from hw2a.Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(2,2,2),'Equilateral','2,2,2 should be equilateral')
          
    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(4,5,6),'Scalene','4,5,6 should be scalene')
    
    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(3,5,7),'Scalene','3,5,7 should be scalene')
         
    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(5,5,9),'Isosceles','5,5,9 should be isosceles')
      
    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(4,4,7),'Isosceles','4,4,7 should be isosceles')
       
    def testNotATriangleA(self): 
        self.assertEqual(classifyTriangle(2,3,7),'NotATriangle','2,3,7 should be NotATriangle')
       
    def testNotATriangleB(self): 
        self.assertEqual(classifyTriangle(3,4,9),'NotATriangle','3,4,9 should be NotATriangle')
       
    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(250,300,-350),'InvalidInput','250,300,-350 should be InvalidInput')
        
    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle('three',4,5),'InvalidInput','three,4,5 should be InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

