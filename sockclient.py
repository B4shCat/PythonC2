import socket

host_ip = '127.0.0.1'
host_port = 2222

# Create socket object for IPv4 Connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'[+] Connection to {host_ip}.')
sock.connect((host_ip, host_port))
print(f'[+] Connected to {host_ip}.')
sock.close()
