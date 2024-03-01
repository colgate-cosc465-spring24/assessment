#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsSubnet(unittest.TestCase):
    def test_yes_ipv6(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv6Network('FC00::/7'),
                ipaddress.IPv6Network('FC10::/16'))
        self.assertTrue(actual, "is_subnet(FC00::/7, FC10::/16) should be True")

if __name__ == '__main__':
    unittest.main()
