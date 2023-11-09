import socket

# Binds host ip and port to the socket and begins listening for a connection
def listen_handler():
    sock.bind((host_ip, host_port))
    print('[+] Awaiting connection from client...')
    sock.listen()
    remote_target, remote_ip = sock.accept()
    print(f'[+] Connection received from {remote_ip[0]}')
    while True:
        # try/catch to ensure connection is closed
        try:
            message = input('Message to send #> ')
            # Exit message handler
            if message.lower() == 'exit':
                print('[+] Closing connecition...')
                remote_target.send(message.encode())
                remote_target.close()
                break

            # Message must be encoded so both sides know how to read it
            remote_target.send(message.encode())
            response = remote_target.recv(1024).decode()
            # exit message from remote host handler
            if response.lower() == 'exit':
                print('[+] Connection closed from remote client')
                remote_target.close()
                break

            print(response)
        except KeyboardInterrupt:
            print("\n[+] Keyboard Interrupt issued")
            remote_target.close()
            break

        except Exception:
            remote_target.close()
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '127.0.0.1'
host_port = 2222
listen_handler()
