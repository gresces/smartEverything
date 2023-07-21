import socket

def main():
    #  1.创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
    # 2.必须选择接收时的ip和端口 (ip,端口)
    local_address = ('192.168.244.41', 6666)
    udp_socket.bind(local_address)
 
    while True:
        # 3.接收对方发送的数据
        # recv_data = udp_socket.recvfrom(1024)
        # recv_msg = recv_data[0].decode('utf-8')
        # recv_address = recv_data[1]
        # print('当前客户端地址：{}，当前接受的信息是：{}'.format(recv_address, recv_msg))
 
        # 发送数据到指定的电脑
        send_addr = '192.168.244.214'
        send_port = 8080
        info = "TO" + "["+ send_addr + ":" + str(send_port)+"]" + ":"
        send_data = input(info)
        udp_socket.sendto(send_data.encode('utf-8'), (send_addr , send_port))
        if send_data == 'exit':
            break
    # 4.关闭套接字
    udp_socket.close()
 
 
if __name__ == '__main__':
    main()
