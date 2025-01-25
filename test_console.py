#!/usr/bin/python3
import unittest

class TestConsole(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual("hello", "hello")

if __name__ == '__main__':
    unittest.main()
