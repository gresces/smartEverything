import html
import socket

def SocketCilentSend():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
    local_address = ('', 8080)
    udp_socket.bind(local_address)
    to = ('120.48.100.193', 3210)
    while True:
        send_data = input('>>')
        udp_socket.sendto(send_data.encode('utf-8'), to)
        if send_data == "exit":
            break