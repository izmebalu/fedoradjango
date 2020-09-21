import unittest
class Testdemo(unittest.TestCase):
    def setUp(self):
        print("setupmethod execution")
    def test1(self):
        print("testmesthod exection")
    def test2(self):
        print("testmesthod exection")
    def tearDown(self):
        print("teardown execution")

unittest.main()