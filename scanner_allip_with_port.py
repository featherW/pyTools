#!/usr/bin/env python
#form http://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python/
import socket
import subprocess
import sys
import thread
import time
from datetime import datetime

def scan_port_for_ip(remote_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remote_ip, port))
        if result == 0:
            print 'IP{%s} Port{%d}: OPEN.'%(remote_ip, port)
            sock.close()
            return True
    except socket.error:
        print "Couldn't connect to server"
        return False

def scan_main(ip_str, port):
    server_ip = "".join(ip_str)
    scan_port_for_ip(server_ip, port)

def find_ip(ip_prefix, port):
    for i in range(1, 256):
        ip = '%s.%s'%(ip_prefix, i)
        thread.start_new_thread(scan_main, (ip,port))
        time.sleep(0.3)

if __name__ == "__main__":
    try:
        commandargs = sys.argv[1:]
        args = "".join(commandargs)
        ip_prefix = '.'.join(args.split('.')[:-1])

        commandargs2 = sys.argv[2:]
        if len(commandargs2) == 0:
            port = "80"
        else:
            port = "".join(commandargs2)

        find_ip(ip_prefix, int(port))
    except KeyboardInterrupt:                                                                                                                                                             
        print "You pressed Ctrl+C"
        sys.exit()
