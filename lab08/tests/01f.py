#!/usr/bin/env python3

import random
import stop_and_wait
import socket
import unittest
from unittest import mock
import mocking
import datetime

class TestSender(unittest.TestCase):
    def test_01f(self):
        # Create server socket
        port = random.randint(10000,60000)
        sock = socket.socket(type=socket.SOCK_DGRAM)
        sock.settimeout(2)
        sock.bind(("", port))

        # Send data with mocked timers
        with mock.patch('threading.Timer', side_effect=mocking.MockTimer) as mock_method:
            sender = stop_and_wait.Sender(("127.0.0.1", port)) 
            sender.send(b"First")
            sent = datetime.datetime.now()

            try:
                raw, _ = sock.recvfrom(1000)
                self.assertTrue(b"First" in raw)
                raw, _ = sock.recvfrom(1000)
                self.assertTrue(b"First" in raw)
                recv = datetime.datetime.now()
                elapsed = recv - sent
                self.assertAlmostEqual(elapsed.total_seconds(), 1, places=1)
            finally:
                mocking.cancel_timers()
                sock.close()

if __name__ == '__main__':
    unittest.main()
