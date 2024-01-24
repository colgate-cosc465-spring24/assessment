#!/usr/bin/env python3

import unittest
import terminology
import inspect

class TermTests(unittest.TestCase):
    def test_str(self):
        members = {name : obj for name, obj in inspect.getmembers(terminology.Term)}
        self.assertEqual(str(type(members['__str__'])), "<class 'function'>", msg="Term class should contain a __str__ method")

        term1 = terminology.Term("Address Resolution Protocol")
        self.assertEqual(str(term1), "Address Resolution Protocol (ARP)", "__str__method in Term class should return a string with the term and acronym")

if __name__ == '__main__':
    unittest.main()