import socket
data =0
TCP_IP = '192.168.1.8'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while data != "stop":
    data = conn.recv(BUFFER_SIZE).decode()
    if not data: break
    print ("received data:", data)
    conn.send(data.encode())  # echo
conn.close()
