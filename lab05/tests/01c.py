#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsSubnet(unittest.TestCase):
    def test_yes_same_prefix_prefixlen_plus_one(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('172.16.0.0/16'),
                ipaddress.IPv4Network('172.16.0.0/17'))
        self.assertTrue(actual, "is_subnet(172.16.0.0/16, 172.16.0.0/17) should be True")

if __name__ == '__main__':
    unittest.main()
