## Interface ##
## v 0.9 ##

import tcp

def inter(remote_ip, port, data=""):
    rep = 0
    #Can be IP or domain name
    #remote_ip = input("Host address: ")

    #The port that you want to connect to
    #port = int(input("Input Port: "))
        
    #data = input("Enter data: ")
    if data != "":
        s = tcp.connect(remote_ip, port)
        
        if s != False:
            #Send data
            if not tcp.send(data, s):
                return False
            
            #Receive data
            rep = tcp.receive(s)
            
            if rep == False:
                print("error disconnected")
                return False
            else:
                s.close()
                return rep
                
        else:
            print("An error has occured")
            return False
    else:
        return False

ip = '192.168.1.11'
port = 5050
info = inter(ip, port,data=input("Enter Data: "))
print(info)
