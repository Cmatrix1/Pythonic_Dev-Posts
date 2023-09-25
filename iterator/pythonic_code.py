# # Echo server program
# import socket

# HOST = ''                 # Symbolic name meaning all available interfaces
# PORT = 50007              # Arbitrary non-privileged port



# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen(1)
#     conn, addr = s.accept()
#     with conn:
#         print('Connected by', addr)
#         while True:
#             data = conn.recv(1024)
#             if not data: break
#             conn.sendall(data)


# def echo_server():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen(1)
#         conn, addr = s.accept()
#         with conn:
#             print('Connected by', addr)
#             for data in iter(lambda: conn.recv(1024), b''):
#                 conn.sendall(data)


# Without iter:
with open("test.txt") as f:
    while True:
        chunk = f.read(12)
        if chunk == "":
            break
        print(chunk)

# With iter:
with open("test.txt") as f:
    method = lambda: f.read(12)
    for data in iter(method, ""):
        print(data)

