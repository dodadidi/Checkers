import unittest
import main
import os
import subprocess

class TestStringMethods(unittest.TestCase):

    def test_getLevel(self):
        
        var=main.get_level()
        self.assertTrue(var==1 or var==2 or var==3 and isinstance(var,int))

if __name__ == '__main__':
    unittest.main()