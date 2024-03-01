#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsAdjacent(unittest.TestCase):
    def test_yes_address(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('172.16.15.0/25'),
                ipaddress.IPv4Network('172.16.15.128/32'))
        self.assertTrue(actual, "is_adjacent(172.16.15.0/25, 172.16.15.128/32) should be True")

if __name__ == '__main__':
    unittest.main()
