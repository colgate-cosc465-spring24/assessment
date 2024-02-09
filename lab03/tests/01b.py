#!/usr/bin/env python3

import unittest
import client_bot
import inspect

class TestMessenger(unittest.TestCase):
    def test_client_bot_http_version(self):
        source, _ = inspect.getsourcelines(client_bot.send_request)
        for line in source:
            if "first = " in line:
                print(line, end="")
                self.assertTrue("HTTP/1.1" in line, "Initialization of first line of HTTP request must include HTTP version")

if __name__ == '__main__':
    unittest.main()
