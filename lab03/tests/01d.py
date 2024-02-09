#!/usr/bin/env python3

import unittest
import client_bot
import inspect

class TestMessenger(unittest.TestCase):
    def test_client_bot_line_separator(self):
        source, _ = inspect.getsourcelines(client_bot.send_request)
        for line in source:
            if "request =" in line and "join" in line:
                print(line, end="")
                self.assertTrue('"\\r\\n"' in line, "Lines in request must be separated by \\r\\n")

if __name__ == '__main__':
    unittest.main()
