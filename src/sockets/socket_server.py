import socket

HOST = '127.0.0.1'
PORT = 65432
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(
    (HOST, PORT)
)

max_clients = 5
s.listen(max_clients)
clients_counter = 0
while True:
    print(f'Waiting for client num #{clients_counter} ...')
    conn, addr = s.accept()
    print(f'Connected by {addr}')
    data = conn.recv(1024)
    conn.sendall(data)
    conn.close()
    clients_counter += 1
