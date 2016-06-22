#!/usr/bin/env python
#form http://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python/
import socket
import subprocess
import sys
from datetime import datetime

def scan_port_for_ip(remote_ip):
    try:
        for port in range(1, 65536):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remote_ip, port))
            if result == 0:
                print "Port{%d}: OPEN."%port
            sock.close()
    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

if __name__ == "__main__":
    try:
        # Clear the screen
        subprocess.call('clear', shell=True)
        t1 = datetime.now()

        args = sys.argv[1:]
        server_ip = "".join(args)
        scan_port_for_ip(server_ip)

        t2 = datetime.now()
        total =  t2 - t1
        print 'Scanning Completed in: ', total
    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()  
