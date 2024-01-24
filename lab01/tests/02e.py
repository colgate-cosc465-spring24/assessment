#!/usr/bin/env python3

import unittest
import terminology
import inspect

class GlossaryTests(unittest.TestCase):
    def test_lookup_by_keyword(self):
        members = {name : obj for name, obj in inspect.getmembers(terminology.Glossary)}
        self.assertIn('lookup_by_keyword', members, msg="Glossary class should contain a lookup_by_keyword method")
        self.assertTrue(inspect.isfunction(members['lookup_by_keyword']), msg="Glossary class should contain a lookup_by_keyword method")

        signature = inspect.signature(terminology.Glossary.lookup_by_keyword)
        params = signature.parameters
        self.assertGreaterEqual(len(params), 2, msg="lookup_by_keyword method in Glossary class should take two parameters")
        self.assertIn('self', params, msg="self should be a parameter for the lookup_by_keyword method in the Glossary class")

        glossary1 = terminology.Glossary()
        term1 = terminology.Term("Transport Layer Security", ["transport layer", "protocol"])
        term2 = terminology.Term("Address Resolution Protocol", ["network layer", "protocol"])
        glossary1.add(term1)
        glossary1.add(term2)

        self.assertEqual(glossary1.lookup_by_keyword("transport layer"), [term1], "the lookup_by_keyword  method in the Glossary class should return a list of Term objects with a keyword that exactly matches the provided keyword")

        self.assertEqual(glossary1.lookup_by_keyword("network"), [term2], "the lookup_by_keyword  method in the Glossary class should return a list of Term objects with a keyword that partially matches the provided keyword")

        self.assertTrue(glossary1.lookup_by_keyword("protocol") == [term2, term1] or glossary1.lookup_by_keyword("protocol") == [term1, term2], "the lookup_by_keyword method in the Glossary class should return a list of matching Term objects")

if __name__ == '__main__':
    unittest.main()