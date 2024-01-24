#!/usr/bin/env python3

import unittest
import terminology
import inspect

class GlossaryTests(unittest.TestCase):
    def test_add(self):
        members = {name : obj for name, obj in inspect.getmembers(terminology.Glossary)}
        self.assertIn('add', members, msg="Glossary class should contain an add method")
        self.assertTrue(inspect.isfunction(members['add']), msg="Glossary class should contain an add method")

        signature = inspect.signature(terminology.Glossary.add)
        params = signature.parameters
        self.assertGreaterEqual(len(params), 2, msg="add method in Glossary class should take two parameters")
        self.assertIn('self', params, msg="self should be a parameter for the add method in the Glossary class")

        glossary1 = terminology.Glossary()
        term1 = terminology.Term("Address Resolution Protocol")
        glossary1.add(term1)

        instance_vars = glossary1.__dict__
        terms = list(instance_vars.values())[0]
        self.assertIsInstance(terms, dict, "Glossary class should contain an instance variable that is a dictionary")
        self.assertIn('ARP', terms, "term added to Glossary should appear in the dictionary instance variable with the term's acronym as the key")
        self.assertEqual(terms['ARP'], term1, "term added to Glossary should appear in the dictionary instance variable with the term as the value")

        term2 = terminology.Term("Transport Layer Security")
        glossary1.add(term2)
        self.assertIn('TLS', terms, "term added to Glossary should appear in the dictionary instance variable with the term's acronym as the key")
        self.assertEqual(terms['TLS'], term2, "term added to Glossary should appear in the dictionary instance variable with the term as the value")
        self.assertIn('ARP', terms, "adding a term to the Glossary should not remove previously added terms")
        self.assertEqual(terms['ARP'], term1, "adding a term to the Glossary should not change previously added terms")

if __name__ == '__main__':
    unittest.main()