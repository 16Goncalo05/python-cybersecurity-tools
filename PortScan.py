import socket
import sys
from datetime import datetime
import threading

#Target configuration - Replace with your target IP or hostname (e.g., "192.168.1.1")
target = "192.168.1.10"  

def port_scan(port):
    try:
        #Initialize socket: AF_INET specifies IPv4, SOCK_STREAM specifies TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #Set a 1-second timeout so the script doesn't hang on closed ports
        s.settimeout(1.0)
        
        #Attempt to connect to the target port
        result = s.connect_ex((target, port))
        
        #Connect_ex returns 0 if the connection was successful
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        
        s.close()
    except Exception:
        #Silently ignore errors to keep the output clean
        pass

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Scan started at: {str(datetime.now())}")
print("-" * 50)

#Spawn threads to scan ports 1 through 1024 concurrently for optimal speed
for port in range(1, 1025):
    thread = threading.Thread(target=port_scan, args=(port,))
    thread.start()