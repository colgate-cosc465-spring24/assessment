#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsAdjacent(unittest.TestCase):
    def test_yes_ipv6(self):
        actual = ipsubnet.is_adjacent(ipaddress.IPv6Network('FC00::/8'),
                ipaddress.IPv6Network('FD00::/8'))
        self.assertTrue(actual, "is_adjacent(FC00::/8, FD00::/8) should be True")

if __name__ == '__main__':
    unittest.main()
