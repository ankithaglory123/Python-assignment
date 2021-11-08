import unittest
from service.greatest import greatest


class greatesttest(unittest.TestCase):
    def testgreatest1(self):
        self.assertEqual(greatest(0, 0,0), 0)

    def testgreatest2(self):
        self.assertEqual(greatest(1,2,3), 3)

    def testgreatest3(self):
        self.assertEqual(greatest(-1, 9 , 7), 9)

    def testgreatest4(self):
        self.assertEqual(greatest("A", 3,7), None)

        def testgreatest4(self):
            self.assertEqual(greatest(-1,-2,-3), -1)