import socket

# HOST = socket.gethostname()
HOST = "MHTX-COMP1400"
PORT = 65432

print(f'My hostname is = {HOST}')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(
    (HOST, PORT)
)
str_to_send = 'matay afsaka'
s.sendall(str.encode(str_to_send))
data = s.recv(1024)
s.close()
print(f'Received: {data}')
