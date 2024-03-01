#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsAdjacent(unittest.TestCase):
    def test_yes_larger_prefixlen(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('172.16.15.0/24'),
                ipaddress.IPv4Network('172.16.16.0/22'))
        self.assertTrue(actual, "is_adjacent(172.16.15.0/24, 172.16.16.0/22) should be True")

if __name__ == '__main__':
    unittest.main()
