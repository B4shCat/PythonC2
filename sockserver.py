import socket

# set host IP and port
host_ip = '127.0.0.1'
host_port = 2222

# Create socket object for IPv4 connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host_ip, host_port))
print('[+] Awaiting connection from client...')
sock.listen()
remote_target, remote_ip = sock.accept()
print(f'[+] Connection received from {remote_ip}')
remote_target.close()
