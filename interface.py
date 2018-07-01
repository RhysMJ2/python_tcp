## Interface ##
## v 0.92 ##

import tcp

## Will return False if there is an error
def inter(remote_ip, port, data):
    rep = 0
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

if __name__ == "__main__":
    ip = input("Enter ip to connect to: ")
    port = 5050
    info = inter(ip, port,data=input("Enter Data: "))
    print(info)
