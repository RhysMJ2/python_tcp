## TCP Second Try ##
## Component Connect to other Machine ##

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
    return True
connect("127.0.0.1", 80)
