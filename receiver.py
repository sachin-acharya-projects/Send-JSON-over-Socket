import socket, pickle

HEADERSIZE = 10

socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_.connect((socket.gethostname(), 9090))

while True:
    full_msg = b""
    new_msg = True
    while True:
        msg = socket_.recv(16)
        if new_msg:
            print("New Message \n{}".format(msg[:HEADERSIZE]))
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg
        if len(full_msg)-HEADERSIZE == msglen:
            print(pickle.loads(full_msg[HEADERSIZE:]))
            new_msg = True
            full_msg = b""

print(full_msg)