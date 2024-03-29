#!/usr/bin/env python3

import random
import stop_and_wait
import socket
import unittest
from unittest import mock
import mocking
import threading

class TestSender(unittest.TestCase):
    def test_01d(self):

        # Create server socket
        port = random.randint(10000,60000)
        sock = socket.socket(type=socket.SOCK_DGRAM)
        sock.settimeout(1)
        sock.bind(("", port))

        # Send data with mocked timers
        with mock.patch('threading.Timer', side_effect=mocking.MockTimer) as mock_method:
            sender = stop_and_wait.Sender(("127.0.0.1", port)) 
            sender.send("Data1".encode())

            send_thread = threading.Thread(target=sender.send, args=["Data2".encode()])
            send_thread.daemon = True
            send_thread.start()
            send_thread.join(timeout=0.5)
            self.assertTrue(send_thread.is_alive())

            mocking.cancel_timers()
            sock.close()
    
if __name__ == '__main__':
    unittest.main()
