import socket

# Binds host ip and port to the socket and begins listening for a connection
def listen_handler():
    sock.bind((host_ip, host_port))
    print('[+] Awaiting connection from client...')
    sock.listen()
    remote_target, remote_ip = sock.accept()
    print(f'[+] Connection received from {remote_ip[0]}')
    message = input('Message to send #> ')
    # Message must be encoded so both sides know how to read it
    remote_target.send(message.encode())
    response = remote_target.recv(1024).decode()
    print(response)
    remote_target.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1'
host_port = 2222
listen_handler()
