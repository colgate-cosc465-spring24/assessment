#!/usr/bin/env python3

import random
import stop_and_wait
import socket
import unittest
from unittest import mock
import mocking
import threading

class TestSender(unittest.TestCase):
    def test_01l(self):
        # Create server socket
        port = random.randint(10000,60000)
        sock = socket.socket(type=socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.bind(("", port))

        # Send data with mocked timers
        with mock.patch('threading.Timer', side_effect=mocking.MockTimer) as mock_method:
            sender = stop_and_wait.Sender(("127.0.0.1", port)) 

            try:
                sender.send(b"First")
                send_thread = threading.Thread(target=sender.send, args=[b"Second"])
                send_thread.daemon = True
                send_thread.start()

                raw, addr = sock.recvfrom(1000)
                self.assertTrue(b"First" in raw)
                first_pkt = stop_and_wait.Packet.from_bytes(raw)
                sock.sendto(stop_and_wait.Packet(stop_and_wait.PacketType.ACK, first_pkt.seq_num).to_bytes(), addr)

                send_thread.join(timeout=0.5)
                self.assertFalse(send_thread.is_alive())
            finally:
                mocking.cancel_timers()
                sock.close()
    
if __name__ == '__main__':
    unittest.main()
