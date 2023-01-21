import socket

def port_scanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f'Port {port} is open.')
        else:
            print(f'Port {port} is closed.')
        sock.close()
    except:
        print(f'Unable to connect to {host}:{port}')

host = input('Enter the host to scan: ')
port_start = int(input('Enter the starting port: '))
port_end = int(input('Enter the ending port: '))

for port in range(port_start, port_end + 1):
    port_scanner(host, port)
