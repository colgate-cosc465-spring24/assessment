#!/usr/bin/env python3

import unittest
import terminology
import inspect

class GlossaryTests(unittest.TestCase):
    def test_lookup_by_acronym(self):
        members = {name : obj for name, obj in inspect.getmembers(terminology.Glossary)}
        self.assertIn('lookup_by_acronym', members, msg="Glossary class should contain a lookup_by_acronym method")
        self.assertTrue(inspect.isfunction(members['lookup_by_acronym']), msg="Glossary class should contain a lookup_by_acronym method")

        signature = inspect.signature(terminology.Glossary.lookup_by_acronym)
        params = signature.parameters
        self.assertGreaterEqual(len(params), 2, msg="lookup_by_acronym method in Glossary class should take two parameters")
        self.assertIn('self', params, msg="self should be a parameter for the lookup_by_acronym method in the Glossary class")

        glossary1 = terminology.Glossary()
        term1 = terminology.Term("Transport Layer Security")
        term2 = terminology.Term("Address Resolution Protocol")
        glossary1.add(term1)
        glossary1.add(term2)

        self.assertEqual(glossary1.lookup_by_acronym("TLS"), term1, "the lookup_by_acronym method in the Glossary class should return the corresponding term if the acronym exists in the glossary")

        self.assertEqual(glossary1.lookup_by_acronym("IETF"), None, "the lookup_by_acronym method in the Glossary class should return None term if the acronym does not exist in the glossary")

if __name__ == '__main__':
    unittest.main()