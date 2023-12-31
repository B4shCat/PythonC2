import socket
import sys
import threading

def banner():
    print(' _______                   __   ______') 
    print('|       \                 |  \ /      \\  2') 
    print('| $$$$$$$\  ______    ____| $$|  $$$$$$\\')
    print('| $$__/ $$ |      \  /      $$| $$   \$$')
    print('| $$    $$  \$$$$$$\|  $$$$$$$| $$     By B4shCat') 
    print('| $$$$$$$\ /      $$| $$  | $$| $$   __') 
    print('| $$__/ $$|  $$$$$$$| $$__| $$| $$__/  \\')
    print('| $$    $$ \$$    $$ \$$    $$ \$$    $$')
    print(' \$$$$$$$   \$$$$$$$  \$$$$$$$  \$$$$$$') 



def comm_in(targ_id):
    print(f'[+] Awaiting response...')
    response = targ_id.recv(1024).decode()
    return response

def comm_out(targ_id, message):
    targ_id.send(message.encode())

def listen_handler():
    sock.bind((host_ip, host_port))
    print('[+] Awaiting connection from client...')
    sock.listen()
    t1 = threading.Thread(target=comm_handler)
    t1.start()

def comm_handler():
    while True:
        try:
            remote_target, rempte_ip = sock.accept()
            targets.append([remote_target, remote_ip[0]])
            print(f'\n[+] Remote connection from {remote_ip[0]}\n#> ')
        except:
            pass

def target_comm(targ_id):
    while True:
        message = input('Send message #> ')
        comm_out(targ_id, message)
        if message.lower() == 'exit':
            targ_id.send(message.encode())
            targ_id.close()
            break
        if message == 'background':
            break
        else:
            response = comm_in(targ_id)
            if response.lower() == 'exit':
                print('\nClient has closed the session')
                targ_id.close()
                break
            print(response)

# Binds host ip and port to the socket and begins listening for a connection
if __name__ == '__main__':
    targets = []
    banner()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host_ip = "127.0.0.1"
        host_port = 2222
    except IndexError:
        print('[-] Command line arguments not supplied')
    except Exception as e:
        print(e)
    listen_handler()
    while True:
        try:
            command = input('#>')
            if command.split(' ')[0] == 'sessions':
                session_counter = 0
                if command.split(' ')[1] == '-l':
                    print('session' + ' ' * 10 + 'target')
                    for target in targets:
                        print(str(session_count) + ' ' * 16 + target[1])
                        session_counter += 1
                if command.split(' ')[1] == '-i':
                    num = int(command.split(' ')[2])
                    targ_id = (targets[num])[0]
                    target_comm(targ_id)
        except KeyboardInterrupt:
            print('\n[-] Keyboard Interrupt Issued')
            sock.close()
            break
