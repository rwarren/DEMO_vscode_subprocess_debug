import unittest
import socket
import subprocess
import time

class TestEchoServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the echo server
        cls.server_process = subprocess.Popen(["python", "app.py"])
        time.sleep(1)

    def _send_msg(self, msg, host='127.0.0.1', port=5001):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.sendall(msg.encode('utf-8'))
            response = client_socket.recv(1024)
            return response.decode('utf-8')

    def test_echo_message(self):
        message = "Hello, Echo Server!"
        response = self._send_msg(message)
        self.assertEqual(response, message)

    def test_echo_another_message(self):
        message = "Another message"
        response = self._send_msg(message)
        self.assertEqual(response, message)


if __name__ == "__main__":
    unittest.main()
