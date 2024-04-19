#!/usr/bin/env python3

import random
import sliding_window
import socket
import unittest
from unittest import mock
import mocking

class TestSender(unittest.TestCase):
    def test_01i(self):
        # Create server socket
        port = random.randint(10000,60000)
        sock = socket.socket(type=socket.SOCK_DGRAM)
        sock.settimeout(2)
        sock.bind(("", port))

        # Send data with mocked timers
        with mock.patch('threading.Timer', side_effect=mocking.MockTimer) as mock_method:
            sender = sliding_window.Sender(("127.0.0.1", port)) 
            try:
                sender.send(b"First")
                raw, addr = sock.recvfrom(1000)
                self.assertTrue(b"First" in raw)
                first_pkt = sliding_window.Packet.from_bytes(raw)
                sock.sendto(sliding_window.Packet(sliding_window.PacketType.ACK, first_pkt.seq_num, 5).to_bytes(), addr)

                # No retransmission should occur
                timeout = False
                try:
                    raw, _ = sock.recvfrom(1000)
                except socket.timeout:
                    timeout = True
                self.assertTrue(timeout)
            finally:
                mocking.cancel_timers()
                sock.close()

if __name__ == '__main__':
    unittest.main()
