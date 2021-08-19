import socket, pickle

HEADERSIZE = 10

data = {
    "tag": "General",
    "subject": "Message Sent!",
    "message": "Hello, There!"
}

socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_.bind((socket.gethostname(), 9090))
socket_.listen(5)

while True:
    client_socket, client_address = socket_.accept()
    print("Connect has been made {}".format(client_address))

    msg = pickle.dumps(data)
    msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg

    client_socket.send(msg)
