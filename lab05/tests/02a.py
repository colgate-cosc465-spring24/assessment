#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsAdjacent(unittest.TestCase):
    def test_yes_same_prefixlen(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('172.16.15.0/24'),
                ipaddress.IPv4Network('172.16.16.0/24'))
        self.assertTrue(actual, )

if __name__ == '__main__':
    unittest.main()
