import unittest

from no_dupes import no_dupes


class TestNoDupes(unittest.TestCase):

    def test_no_dupes(self):
        x = no_dupes("")
        self.assertTrue(x == "")
        x = no_dupes("hello")
        self.assertTrue(x == "hello")
        x = no_dupes("hello hello")
        self.assertTrue(x == "hello")
        x = no_dupes("cats dogs fish cats dogs")
        self.assertTrue(x == "cats dogs fish")
        x = no_dupes("spam spam spam eggs spam sausage spam spam and spam")
        self.assertTrue(x == "spam eggs sausage and")


if __name__ == '__main__':
    unittest.main()
