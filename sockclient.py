import socket

# Forms connection to server with IP and port
def session_handler():
    print(f'[+] Connection to {host_ip}.')
    sock.connect((host_ip, host_port))
    print(f'[+] Connected to {host_ip}.')
    # message must be decoded since it is sent in bytes
    while True:
            try:
                message = sock.recv(1024).decode()
                # exit message handler
                if message.lower() == 'exit':
                    print('[+] Connection closed from remote host')
                    sock.close()
                    break
                print(message)
                message = input('Message to send #> ')
                # Exit message handler
                if message.lower() == 'exit':
                    print('[+] Closing connection...')
                    sock.send(message.encode())
                    sock.close()
                    break
                sock.send(message.encode())
            except KeyboardInterrupt:
                print("\n[+] Keyboard Interrupt Issued")
                sock.close()
                break
            except Exception:
                sock.close()
                break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1'
host_port = 2222
session_handler()
