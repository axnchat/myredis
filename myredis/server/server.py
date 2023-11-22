import socket
import threading

import typer
from typing_extensions import Annotated

from myredis.commands import handle_command
from myredis.protocol import encode_message, extract_frame_from_stream
from myredis.types_1 import Array, BulkString

class Server:
    def __init__(self, port):
        self.port = port
        self._running = False

    def handle_client(self, client_socket, client_address):
        buffer = bytearray()

        try:
            while True:
                # TODO: Add code to handle the client connection.
                print(f"Handling connection from {client_address}")
                data = client_socket.recv(1024)
                if not data:
                    break

                # TODO: do something with the data.
                # Example: Echoing the received data back to the client.
                #client_socket.sendall(data)            

                buffer.extend(data)

                frame, frame_size = extract_frame_from_stream(buffer)

                if frame:
                    buffer = buffer[frame_size:]
                    result = handle_command(frame)
                    client_socket.send(encode_message(result))
            
        finally:
            # Close the client socket
            client_socket.close()
            print(f"Connection with {client_address} closed")

    def run(self):
        self._running = True

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            self._server_socket = server_socket
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            server_socket.bind(('localhost', self.port))
            server_socket.listen()

            print(f"Server listening on port {self.port}")

            while self._running:
                client_socket, client_address = server_socket.accept()
                print(f"Accepted connection from {client_address}")

                # Spawn a new thread for handling the client connection
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()

    def stop(self):
        self._running = False

# Example usage:
""" if __name__ == "__main__":
    server = Server(port=6379)
    server.run() """
