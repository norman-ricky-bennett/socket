#! /usr/bin/env python3
# This is an example of a simple tcp socket using python


import socket

target_host = "www.google.com"
target_port = 80

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client 
client.connect((target_host, target_port))

# send some data 
client.send("GET / HTTP/1.1\r\n\r\n")

# receive some data
response = client.recv(4096)

print response

