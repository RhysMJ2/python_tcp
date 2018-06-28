## TCP Easy Setup Module v0.9##
## Component Connect to other Machine ##
## R. M. Jones ##

import socket
import sys
import re

def validate(Type, data):
    ip = re.compile("^[0-9]{1,3}[.]{1}[0-9]{1,3}[.]{1}[0-9]{1,3}[.]{1}$")

    if Type == 'ip':
        if ip.match(data):
            return True
        else:
            return False
    
    else:
        return "No Type: "+Type
    
#if domain name is sent then it is resolved here
def domain(host):
    try:
        remote_ip = socket.gethostbyname(host)
        return remote_ip
    
    except socket.gaierror:
        print("Host name could not be resolved")
        return False

def getmyip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1", 80))
    TCP_IP = s.getsockname()[0]
    s.close()
    return TCP_IP

#The default ip is your local one and port is 5050
def bind(TCP_IP=getmyip(), TCP_PORT=5050):
    s = create()
    s.bind((TCP_IP, TCP_PORT))
    print("Ready to connect on: "+TCP_IP+" on port:", TCP_PORT)
    s.listen(1)
    conn, addr = s.accept()
    print ('Connection address:', addr)
    return conn

def create():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return s
    except socket.error:
        print("Failed to connect")
        return False
    
    
def connect(remote_ip, port):
    
    if not validate('ip', remote_ip):
        remote_ip = domain(remote_ip)
        if remote_ip == False:
            print("Error Resolving Host name")
            return False
        
    print("Connecting to: " + remote_ip+" Port:",port)
    try:
        s.connect((remote_ip, port))
        
    
    except NameError:
        try:
            s = create()
            s.connect((remote_ip, port))
            
        except ConnectionRefusedError:
            print("Connection Refused Error (likely because other machine's port isn't open)")
            return False
        
    except ConnectionRefusedError:
        print("Connection Refused Error (likely because other machine's port isn't open)")
        return False
    
    except:
        print("Unknown Error")
        return False
    print("Socket connected to IP: " + remote_ip)
    return s

def send(data, s):
    try:
        s.sendall(data.encode())
        return True
    except:
        print("Couldn't send data")
        return False

def receive(s, buff=4069):
    try:
        return s.recv(buff).decode()
    
    except ConnectionResetError:
        print("Error ConnectionResetError")
        return False
    
    except ConnectionAbortedError:
        print("Error ConnectionAbortedError")
        return False
#connect(socket.gethostbyname(socket.gethostname()), 5005)
