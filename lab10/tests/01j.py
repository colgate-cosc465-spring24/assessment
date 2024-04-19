#!/usr/bin/env python3

import random
import sliding_window
import socket
import unittest
from unittest import mock
import mocking

class TestSender(unittest.TestCase):
    def test_01j(self):

        # Create server socket
        port = random.randint(10000,60000)
        sock = socket.socket(type=socket.SOCK_DGRAM)
        sock.settimeout(0.5)
        sock.bind(("", port))

        # Send data with mocked timers
        with mock.patch('threading.Timer', side_effect=mocking.MockTimer) as mock_method:
            sender = sliding_window.Sender(("127.0.0.1", port)) 
            sender.send(b"First")
            sender.send(b"Second")
            sender.send(b"Third")
            sender.send(b"Fourth")

            try:
                raw, source = sock.recvfrom(1000)
                self.assertTrue(b"First" in raw)
            except socket.timeout:
                self.fail("Should not timeout when receiving first data packet")
            finally:
                mocking.cancel_timers()

            ack = sliding_window.Packet(sliding_window.PacketType.ACK, 0, 2)
            sock.sendto(ack.to_bytes(), source)

            try:
                raw, _ = sock.recvfrom(1000)
                self.assertTrue(b"Second" in raw)
                raw, _ = sock.recvfrom(1000)
                self.assertTrue(b"Third" in raw)
            except socket.timeout:
                self.fail("Should not timeout when receiving second or third data packet")
            finally:
                mocking.cancel_timers()

            ack = sliding_window.Packet(sliding_window.PacketType.ACK, 2, 1)
            sock.sendto(ack.to_bytes(), source)

            try:
                raw, _ = sock.recvfrom(1000)
                self.assertTrue(b"Fourth" in raw)
            except socket.timeout:
                self.fail("Should not timeout when receiving fourth data packet")
            finally:
                mocking.cancel_timers()
                sock.close()
            
if __name__ == '__main__':
    unittest.main()
