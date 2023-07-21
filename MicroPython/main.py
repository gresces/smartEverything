import myfunc
import network
import socket

myfunc.ShowFreq()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('Gresces', 'a123456A@')
    while not wlan.isconnected():
        pass
print('Network config:', wlan.ifconfig())

 
def main():
    #  1.创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
    # 可选(接收时的端口 ('',端口))
    local_address = ('', 8080)
    udp_socket.bind(local_address)
 
    while True:
        # 2.发送数据到指定的电脑
        # send_data = input('请输入你要发送的数据:')
        udp_socket.sendto(send_data.encode('utf-8'), ('192.168.244.41', 6666))
        # if send_data == 'exit':
        #     break
 
        # 接收对方发送的数据
        recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
        recv_msg = recv_data[0].decode('utf-8')
        recv_address = recv_data[1]
        # print('From{}，Recv_Msg:{}'.format(recv_address, recv_msg))
        msg = "[" + recv_address[0] + ":" + str(recv_address[1]) + "]" + ": "
        print(msg.strip(), recv_msg.strip())
 
    # 3.关闭套接字
    udp_socket.close()
main()
