#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsSubnet(unittest.TestCase):
    def test_no_address(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv4Network('172.16.15.0/24'),
                ipaddress.IPv4Network('172.16.0.0/16'))
        self.assertFalse(actual, "is_subnet(172.16.15.0/24, 172.16.0.0/16) should be False")

if __name__ == '__main__':
    unittest.main()
