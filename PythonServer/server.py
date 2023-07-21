import socket
import json

data = {
    'state': True,
    'info': '',
    'ip': '',
    'number': 0,
    'light': 0
}

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('', 3210)
    s.bind(addr)
    while True:
        recv_data = s.recvfrom(1024)
        recv_msg = recv_data[0].decode('utf-8')
        recv_address = recv_data[1]

        str_split = recv_msg.split("@")
        msg = "[" + recv_address[0] + ":" + str(recv_address[1]) + "]" + ": "
        print(msg.strip(), str_split[0].strip(), str_split[1].strip(), str_split[2])

        if int(str_split[2]) == 0:
            data['state'] = not data['state'];
            data['info'] = str_split[0];
            data['ip'] = recv_address[0];
            data['number'] = data['number'] + 1;
        else:
            data['light'] = int(str_split[1]);

        with open('../files/data.json', 'w') as f:
            json.dump(data,f)

        if recv_msg.strip() == 'exit':
            break
            s.close()
main()
