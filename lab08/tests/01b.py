#!/usr/bin/env python3

import random
import stop_and_wait
import socket
import unittest
from unittest import mock
import mocking

class TestSender(unittest.TestCase):
    def test_01b(self):

        # Create server socket
        port = random.randint(10000,60000)
        sock = socket.socket(type=socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.bind(("", port))

        # Send data with mocked timers
        with mock.patch('threading.Timer', side_effect=mocking.MockTimer) as mock_method:
            sender = stop_and_wait.Sender(("127.0.0.1", port)) 
            sender.send(b"First")

            try:
                raw, _ = sock.recvfrom(1000)
                packet = stop_and_wait.Packet.from_bytes(raw)
                self.assertEqual(packet.type, stop_and_wait.PacketType.DATA)
                self.assertEqual(packet.data, b"First")
            finally:
                mocking.cancel_timers()
                sock.close()

if __name__ == '__main__':
    unittest.main()
