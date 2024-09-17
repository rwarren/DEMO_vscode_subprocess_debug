import socket

import debugpy  #type:ignore

def start_echo_server(host='0.0.0.0', port=5001):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Echo server is running on {host}:{port}...")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected by {client_address}")
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode('utf-8')}")
                    client_socket.sendall(data)

def listen_for_debugger(wait):
    debugpy.listen(("0.0.0.0", 5678))
    if wait:
        print("Waiting for debugger attach...")
        debugpy.wait_for_client()
        print("DEBUGGER HAS ATTACHED!!")


if __name__ == "__main__":
    listen_for_debugger(wait=False)
    start_echo_server()
