#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsSubnet(unittest.TestCase):
    def test_yes_all_addresses(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('0.0.0.0/0'),
                ipaddress.IPv4Network('172.16.0.0/16'))
        self.assertTrue(actual, "is_subnet(0.0.0.0/0, 172.16.0.0/16) should be True")

if __name__ == '__main__':
    unittest.main()
