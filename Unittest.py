import unittest
from SpecialCharacter import specialcharacter

class TestRules(unittest.TestCase):

    def setUp(self):
        self.ex1 = specialcharacter()

    def tearDown(self):
        pass

    def testrule(self):
        self.assertEqual(self.ex1.special('a=[]'),'a = []')
        self.assertEqual(self.ex1.special2('a,b'), 'a, b')
        self.assertEqual(self.ex1.special2('for i in line :'), 'for i in line: ')
        self.assertEqual(self.ex1.special('a!=b'), 'a != b')
        self.assertEqual(self.ex1.semiclone('a=b;'),'a=b')


if __name__ == '__main__':
    unittest.main()