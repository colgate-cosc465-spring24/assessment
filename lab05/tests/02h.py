#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsAdjacent(unittest.TestCase):
    def test_no_address(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv4Network('172.16.15.0/25'),
                ipaddress.IPv4Network('172.16.15.255/32'))
        self.assertFalse(actual, "is_adjacent(172.16.15.0/25, 172.16.15.255/32) should be False")

if __name__ == '__main__':
    unittest.main()
