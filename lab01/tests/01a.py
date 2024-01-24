#!/usr/bin/env python3

import unittest
import terminology
import inspect

class TermTests(unittest.TestCase):
    def test_constructor(self):
        signature = inspect.signature(terminology.Term.__init__)
        params = signature.parameters
        self.assertEqual(len(params), 3, msg="Constructor for Term class should take three parameters")
        self.assertIn('self', params, msg="self should be a parameter for the Term class constructor")
        self.assertIn('term', params, msg="term should be a parameter for the Term class constructor")
        self.assertIn('keywords', params, msg="keywords should be a parameter for the Term class constructor")
        self.assertEqual(params['keywords'].default, [], msg="the keywords parameter for the Term class constructor should be optional with an empty list as the default value")

        term1 = terminology.Term("Address Resolution Protocol", ["network layer", "protocol"])
        instance_vars = term1.__dict__
        self.assertIn('_term', instance_vars, msg="_term should be an instance variable initialized in the Term class constructor")
        self.assertEqual(instance_vars['_term'], "Address Resolution Protocol", "_term instance variable should be initialized to the term passed to the Term class constructor")
        self.assertIn('_keywords', instance_vars, msg="_keywords should be an instance variable initialized in the Term class constructor")
        self.assertEqual(instance_vars['_keywords'], ["network layer", "protocol"], "_keyords instance variable should be initialized to the keywords passed to the Term class constructor")

        term2 = terminology.Term("Transport Layer Security")
        self.assertEqual(term2.__dict__['_keywords'], [], "_keyords instance variable should be initialized to an empty list if no keywords are passed to the Term class constructor")

if __name__ == '__main__':
    unittest.main()