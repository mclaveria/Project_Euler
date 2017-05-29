import unittest

from Problem030_Digit_Fifth_Powers import sumOfPowerDigits

class testSumOfPowerDigits(unittest.TestCase):
    #Test sumOfPowerDigits function from Problem30
    
    def test_power1(self):
        result = sumOfPowerDigits(1634, 4)
        self.assertEqual(result, 1634)
    
    def test_power2(self):
        result = sumOfPowerDigits(8208, 4)
        self.assertEqual(result, 8208)
        
    def test_power3(self):
        result = sumOfPowerDigits(9474, 4)
        self.assertEqual(result, 9474)
    
    def test_power4(self):
        result = sumOfPowerDigits(54748, 5)
        self.assertEqual(result, 54748)
    
    def test_power5(self):
        result = sumOfPowerDigits(92727, 5)
        self.assertEqual(result, 92727)
        
    def test_power6(self):
        result = sumOfPowerDigits(93084, 5)
        self.assertEqual(result, 93084)

if __name__ == '__main__':
    unittest.main()
    