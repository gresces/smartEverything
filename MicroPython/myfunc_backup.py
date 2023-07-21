import machine
import network
import socket
import urequests
import time

def ShowFreq():
    freq = machine.freq()
    print("This MCU's freq: " , freq / 1000000 , "Mps")

def ConnectWifi(ssid, pwd):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(ssid, pwd)
        while not wlan.isconnected():
            pass
    print('Network config:', wlan.ifconfig())
    
def SocketCilentRecv():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
    local_address = ('', 9876)
    udp_socket.bind(local_address)
 
    while True:
        recv_data = udp_socket.recvfrom(1024)
        recv_msg = recv_data[0].decode('utf-8')
        recv_address = recv_data[1]
        if not recv_msg:
            pass
        msg = "[" + recv_address[0] + ":" + str(recv_address[1]) + "]" + ": "
        print(msg.strip(), recv_msg.strip())
 
    udp_socket.close()
    
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

def GetInfo():
    while True:
        res = urequests.get('http://120.48.100.193:8081/data.json')
        print(res.json()['state'])
        time.sleep(1)
