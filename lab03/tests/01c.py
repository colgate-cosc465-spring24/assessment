#!/usr/bin/env python3

import unittest
import client_bot
import inspect

class TestMessenger(unittest.TestCase):
    def test_client_bot_user_agent(self):
        source, _ = inspect.getsourcelines(client_bot.send_request)
        for line in source:
            if "agent = " in line:
                print(line, end="")
                self.assertTrue("User-Agent:" in line, "Agent variable must be initialized with properly formtted User-Agent option")

if __name__ == '__main__':
    unittest.main()
