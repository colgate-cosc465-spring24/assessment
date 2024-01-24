#!/usr/bin/env python3

import unittest
import terminology
import inspect

class TermTests(unittest.TestCase):
    def test_keywords(self):
        members = {name : obj for name, obj in inspect.getmembers(terminology.Term)}
        self.assertIn('keywords', members, msg="Term class should contain a keywords method")
        self.assertIsInstance(members['keywords'], property, msg="keywords should be a property method in the Term class")


        term1 = terminology.Term("Address Resolution Protocol", ["network layer", "protocol"])
        self.assertEqual(term1.keywords, ["network layer", "protocol"], "keywords property method in the Term class should return a list of the keywords")

        term2 = terminology.Term("Transport Layer Security", ["transport layer", "protocol"])
        self.assertEqual(term2.keywords, ["protocol", "transport layer"], "keywords property method in the Term class should return a SORTED list of the keywords")

if __name__ == '__main__':
    unittest.main()