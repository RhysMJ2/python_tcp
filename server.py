import socket
import tcp

def server():
    data =0
    TCP_IP = tcp.getmyip()
    TCP_PORT = int(input("Enter port: "))
    BUFFER_SIZE = 20  # Normally 1024, but we want fast response

    conn = tcp.bind(TCP_IP, TCP_PORT)

    while data != "stop":
        data = tcp.receive(conn, BUFFER_SIZE)
        if not data:
            conn = tcp.bind(TCP_IP, TCP_PORT)
        else:
            print ("received data:", data)
            
            tcp.send(data, conn)
            #conn.send(data.encode())  # enumerate
            
    conn.close()

server()
