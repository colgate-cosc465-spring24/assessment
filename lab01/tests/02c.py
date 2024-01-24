#!/usr/bin/env python3

import unittest
import terminology
import inspect

class GlossaryTests(unittest.TestCase):
    def test_terms(self):
        members = {name : obj for name, obj in inspect.getmembers(terminology.Glossary)}
        self.assertIn('terms', members, msg="Glossary class should contain a terms method")
        self.assertIsInstance(members['terms'], property, msg="terms should be a property method in the Glossary class")

        glossary1 = terminology.Glossary()
        term1 = terminology.Term("Transport Layer Security")
        term2 = terminology.Term("Address Resolution Protocol")
        glossary1.add(term1)
        glossary1.add(term2)

        self.assertEqual(glossary1.terms, [term2, term1], "terms property method in the Glossary class should return a list of term objects sorted in alphabetical ordered by acronym")

if __name__ == '__main__':
    unittest.main()