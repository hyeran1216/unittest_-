import unittest
from unittest.mock import patch
import my_functions

#실제코드
def function1(L):
    total = 0
    for number in L:
        if number%2==1:
            total += number
    return total

def function2(s):
    digits = [int(i) for i in s if i.isdigit()]
    return str(sum(digits)/len(digits))

# 테스트코드
class Test(unittest.TestCase):
    def test_function1(self):
        self.assertEqual(function1([1,2,3]),4)
        self.assertEqual(function1([2, 4, 6, 8]),0)
        self.assertEqual(function1([-3, 1, 3, 2, 100]),1)

    @patch('__main__.function2') 
    def test_function2_with_mock(self, mock_func):
        mock_func.return_value = '2.0'
        self.assertEqual(function2('A1B2C3'), '2.0')
        mock_func.assert_called_once_with('A1B2C3')

        mock_func.return_value = '0.0'
        self.assertEqual(function2('pyt0hon'), '0.0')
        mock_func.assert_called_with('pyt0hon')

# 테스트를 진행
if __name__ == '__main__':
    unittest.main()