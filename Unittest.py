import unittest
from SpecialCharacter import specialcharacter

class TestRules(unittest.TestCase):

    def setUp(self):
        self.ex1 = specialcharacter()

    def tearDown(self):
        pass

    def testrule(self):
        self.assertEqual(self.ex1.special('a=[]'),'a = []')


if __name__ == '__main__':
    unittest.main()