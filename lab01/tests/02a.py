#!/usr/bin/env python3

import unittest
import terminology
import inspect

class GlossaryTests(unittest.TestCase):
    def test_constructor(self):
        members = {name : obj for name, obj in inspect.getmembers(terminology)}
        self.assertIn('Glossary', members, msg="terminology module should contain a Glossary class")
        self.assertTrue(inspect.isclass(members['Glossary']), msg="terminology module should contain a Glossary class")

        members = {name : obj for name, obj in inspect.getmembers(terminology.Glossary)} 
        constructor = members['__init__']
        self.assertNotEqual(str(type(constructor)), "<class 'wrapper_descriptor'>", msg="Glossary class should contain a constructor")

        signature = inspect.signature(terminology.Glossary.__init__)
        params = signature.parameters
        self.assertEqual(len(params), 1, msg="Constructor for Glossary class should take one parameter")
        self.assertIn('self', params, msg="self should be a parameter for the Glossary class constructor") 

        glossary1 = terminology.Glossary()
        instance_vars = glossary1.__dict__
        self.assertEqual(len(instance_vars), 1, msg="Constructor for Glossary class should initialize an instance variable")
        self.assertEqual(list(instance_vars.values())[0], {}, msg="Constructor for Glossary class should initialize an instance variable to an empty dictionary") 

if __name__ == '__main__':
    unittest.main()