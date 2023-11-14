import socket
import sys

def comm_in(remote_target):
    print(f'[+] Awaiting response...')
    response = remote_target.recv(1024).decode()
    return response

def comm_out(remote_target, message):
    remote_target.send(message.encode())

def listen_handler():
    sock.bind((host_ip, host_port))
    print('[+] Awaiting connection from client...')
    sock.listen()
    remote_target, remote_ip = sock.accept()
    comm_handler(remote_target, remote_ip)

def comm_handler(remote_target, remote_ip):
    print(f'Connection received from {remote_ip[0]}')
    while True:
        # try/catch to ensure connection is closed
        try:
            message = input('Message to send #> ')
            # Exit message handler
            if message.lower() == 'exit':
                print('[+] Closing connecition...')
                comm_out(remote_target, message)
                remote_target.close()
                break
            comm_out(remote_target, message)
            response = comm_in(remote_target)
            if response.lower() == 'exit':
                print('[+] Connection closed by remote host')
                remote_target.close()
                break
            print(response)
        except KeyboardInterrupt:
            print('[+] Keyboard Interrupt Issued...')
            remote_target.close()
            break
        except Exception:
            remote_target.close()
            break




# Binds host ip and port to the socket and begins listening for a connection
def listen_handler_old():
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
            
        except KeyboardInterrupt:
            print("\n[+] Keyboard Interrupt issued")
            remote_target.close()
            break

        except Exception:
            remote_target.close()
            break

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = sys.argv[1] 
    host_port = int(sys.argv[2])
    listen_handler()
