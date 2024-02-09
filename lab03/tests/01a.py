#!/usr/bin/env python3

import unittest
import client_bot
import inspect

class TestMessenger(unittest.TestCase):
    def test_client_bot_connect(self):
        source, _ = inspect.getsourcelines(client_bot.main)
        for line in source:
            if "client_sock.connect" in line:
                print(line, end="")
                self.assertTrue("settings.hostname" in line, "Connect call must include hostname from settings")

if __name__ == '__main__':
    unittest.main()
