#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsAdjacent(unittest.TestCase):
    def test_no_ipv6(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv6Network('FC00::/8'),
                ipaddress.IPv6Network('FE00::/8'))
        self.assertFalse(actual, "is_adjacent(FC00::/8, FE00::/8) should be False")

if __name__ == '__main__':
    unittest.main()
