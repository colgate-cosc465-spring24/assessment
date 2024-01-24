#!/usr/bin/env python3

import unittest
import terminology
import inspect

class GlossaryTests(unittest.TestCase):
    def test_lookup_by_keyword(self):
        members = {name : obj for name, obj in inspect.getmembers(terminology.Glossary)}
        self.assertIn('load', members, msg="Glossary class should contain a load method")
        self.assertTrue(inspect.ismethod(members['load']), msg="Glossary class should contain a load class method")

        glossary1 = terminology.Glossary.load(filename="tests/networking.json")

        self.assertGreaterEqual(len(glossary1.terms), 10, "load method in the Glossary class should have loaded 10+ terms from the networking.json file")
        self.assertIsInstance(glossary1.terms[0], terminology.Term, "load method in the Glossary class should have created and added Term objects")

if __name__ == '__main__':
    unittest.main()