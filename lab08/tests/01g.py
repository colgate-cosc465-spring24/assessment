#!/usr/bin/env python3

import random
import stop_and_wait
import socket
import unittest
from unittest import mock
import mocking

class TestSender(unittest.TestCase):
    def test_01g(self):
        # Create server socket
        port = random.randint(10000,60000)
        sock = socket.socket(type=socket.SOCK_DGRAM)
        sock.settimeout(2)
        sock.bind(("", port))

        # Send data with mocked timers
        with mock.patch('threading.Timer', side_effect=mocking.MockTimer) as mock_method:
            sender = stop_and_wait.Sender(("127.0.0.1", port)) 
            sender.send(b"First")

            try:
                raw, _ = sock.recvfrom(1000)
                orig = stop_and_wait.Packet.from_bytes(raw)
                raw, _ = sock.recvfrom(1000)
                retrans = stop_and_wait.Packet.from_bytes(raw)
                self.assertEqual(orig.type, retrans.type)
                self.assertEqual(orig.seq_num, retrans.seq_num)
                self.assertEqual(orig.data, retrans.data)
            finally:
                mocking.cancel_timers()
                sock.close()

if __name__ == '__main__':
    unittest.main()
