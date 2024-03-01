#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsSubnet(unittest.TestCase):
    def test_yes_different_prefix(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('172.16.0.0/16'),
                ipaddress.IPv4Network('172.16.172.0/24'))
        self.assertTrue(actual, "is_subnet(172.16.0.0/16, 172.16.172.0/24) should be True")

if __name__ == '__main__':
    unittest.main()
