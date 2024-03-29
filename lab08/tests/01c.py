#!/usr/bin/env python3

import random
import stop_and_wait
import socket
import unittest
from unittest import mock
import mocking

class TestSender(unittest.TestCase):
    def test_01c(self):

        # Create server socket
        port = random.randint(10000,60000)
        sock = socket.socket(type=socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.bind(("", port))

        # Send data with mocked timers
        with mock.patch('threading.Timer', side_effect=mocking.MockTimer) as mock_method:
            sender = stop_and_wait.Sender(("127.0.0.1", port)) 

            try:
                for i in range(3):
                    sender.send("Data{}".format(i).encode())
                    raw, addr = sock.recvfrom(1000)
                    packet = stop_and_wait.Packet.from_bytes(raw)
                    self.assertEqual(packet.data, "Data{}".format(i).encode())
                    self.assertTrue((packet.seq_num == i or packet.seq_num == i+1 or packet.seq_num == i % 2))
                    sock.sendto(stop_and_wait.Packet(stop_and_wait.PacketType.ACK, packet.seq_num).to_bytes(), addr)
            finally:
                mocking.cancel_timers()
                sock.close()

if __name__ == '__main__':
    unittest.main()
