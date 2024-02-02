#!/usr/bin/env python3

import unittest
import knock
import inspect

class TestKnock(unittest.TestCase):
    def test_server_close(self):
        source, _ = inspect.getsourcelines(knock.main)
        closes = 0
        withs = 0
        for line in source:
            if "close()" in line:
                closes += 1
                print(line, end="")
            if "with" in line and "socket.socket(" in line:
                withs += 1
                print(line, end="")
        self.assertEqual(closes + withs, 1)

if __name__ == '__main__':
    unittest.main()
