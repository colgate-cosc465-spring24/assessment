#!/usr/bin/env python3

import unittest
import ipsubnet
import ipaddress

class TestIsSubnet(unittest.TestCase):
    def test_yes_ipv6(self):
        actual = ipsubnet.is_subnet(ipaddress.IPv6Network('FC00::/7'),
                ipaddress.IPv6Network('FB00::/8'))
        self.assertFalse(actual, "is_subnet(FC00::/7, FB00::/8) should be False")

if __name__ == '__main__':
    unittest.main()
