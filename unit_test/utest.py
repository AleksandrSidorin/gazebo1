#!/usr/bin/env python
import unittest
import numpy as np

def Tz(z):
    Tz = np.array([ [1,0,0,0],
                    [0,1,0,0],
                    [0,0,1,z],
                    [0,0,0,1]])
    return Tz
def Ry(q):
    Rz = np.array([ [np.cos(q),    0,      np.sin(q), 0],
                    [0,            1,      0,         0],
                    [-np.sin(q),   0,      np.cos(q), 0],
                    [    0    ,    0     , 0,         1]])
    return Rz
def FK(d1, q1, q2, d2):
  a = np.array([[0],[0], [0], [1]])
  P=Tz(1).dot(Tz(d1+2).dot(Ry(q1).dot(Tz(2).dot(Ry(q2).dot(Tz(1).dot(Tz(d2+1).dot(a)))))))
  return P[:3]
class Test(unittest.TestCase):
  def test_FK(self):
    d1 = 1
    q1 = 0.5
    q2 = -0.5
    d2 = 0.5
    c = np.array([[0.958851],[0], [8.25516512]])
    self.assertEqual(np.sum((FK(d1, q1, q2, d2)- c) < 0.001), 3)
if __name__ == '__main__':
  unittest.main()



