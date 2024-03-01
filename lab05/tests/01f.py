#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsSubnet(unittest.TestCase):
    def test_yes_large_prefixlen(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('172.16.15.14/31'),
                ipaddress.IPv4Network('172.16.15.15/32'))
        self.assertTrue(actual, "is_subnet(172.16.15.14/31, 172.16.15.15/32) should be True")

if __name__ == '__main__':
    unittest.main()
