#!/usr/bin/env python3

import unittest
import client_bot
import inspect

class TestMessenger(unittest.TestCase):
    def test_client_bot_blank_line(self):
        source, _ = inspect.getsourcelines(client_bot.send_request)
        for line in source:
            if "agent =" in line and "\\r\\n\\r\\n" in line:
                print(line, end="")
                return True
            elif "request =" in line and "join" in line:
                print(line, end="")
                if ('accept, "", ""]' in line 
                        or '+ "\\r\\n\\r\\n"' in line
                        or 'accept, ""]) + "\\r\\n"' in line
                        or 'accept, "\\r\\n"])' in line):
                    return True
            elif "request " in line and "\\r\\n\\r\\n" in line:
                print(line, end = "")
                return True
        self.assertTrue(False, "Blank line (\\r\\n\\r\\n) must be added to the request variable or the accept variable")

if __name__ == '__main__':
    unittest.main()
