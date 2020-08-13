
import unittest

# 1.2 Check Permutation
def check_permutation(str1 : str, str2: str) -> bool:
    str1_list = list(str1)
    for letter in str2:
        if len(str1_list) == 0 or letter not in str1_list:
            return False
        else:
            str1_list.remove(letter)
    if len(str1_list) == 0 : return True
    else: return False



class test_check_permutation(unittest.TestCase):
    def test(self):
        x1 = 'abbac'
        y1 = 'babca'

        x2 = 'abbac'
        y2 = 'babaa'

        self.assertTrue(check_permutation(x1,y1))
        self.assertFalse(check_permutation(x2, y2))

        print("All tests passed")

myTest = test_check_permutation()
myTest.test()