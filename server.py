## Example use of tcp v0.93 ##
## R. M. Jones ##
## 01/07/2017 ##

import tcp  #imoprts the module that is included with this file

def server(BUFFER_SIZE, TCP_IP=tcp.getmyip(), TCP_PORT=5050):
    conn = tcp.bind(TCP_IP, TCP_PORT)
        
    data = tcp.receive(conn, BUFFER_SIZE)
    if not data:
        conn = tcp.bind(TCP_IP, TCP_PORT)
    else:
        return "received data: " + data, conn
    

if __name__ == "__main__":
    info = 0
    s = 0
    while info != "stop":
        try:
            info, s = server(20)
            print(info)
            tcp.send(info, s)    
            s.close()
        except TypeError:
            print("Error, Type Error")
            tcp.send("Repeat", s)
