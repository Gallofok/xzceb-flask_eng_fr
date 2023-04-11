import unittest
from translator import englishToFrench,frenchToEnglish
class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
    def test2(self):
        self.assertNotEqual(frenchToEnglish(" "),"Hello")
class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
    def test2(self):
        self.assertNotEqual(englishToFrench(" "),"Bonjour")
unittest.main()