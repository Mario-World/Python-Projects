import socket 


SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #value - 0 or 1 0 = off and 1 = off.

server_socket.bind(("0.0.0.0", 8080))

server_socket.listen(5)

print(f"Listening on port {SERVER_PORT} ...")

while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(1500).decode()
    print(request)
    
    headers = request.split('\n')
    if not headers or not headers[0].strip():
        client_socket.close()
        continue
    first_header_components = headers[0].split()
    if len(first_header_components) < 2:
        client_socket.close()
        continue

    http_method = first_header_components[0]
    path = first_header_components[1]

    if http_method == 'GET':
        if path == '/':
            fin = open('index.html')
        elif path == '/book':
            fin = open('book.json')
        else:
            # handle the edge case
            response = 'HTTP/1.1 404 Not Found\r\n\r\nPage not found'
            client_socket.sendall(response.encode())
            client_socket.close()
            continue
        
        content = fin.read()
        fin.close()
        response = 'HTTP/1.1 200 OK\r\n\r\n' + content
    else:
        response = 'HTTP/1.1 405 Method Not Allowed\r\nAllow: GET\r\n\r\n'

    client_socket.sendall(response.encode())
    client_socket.close()