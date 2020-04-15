from socket import *

server_address = ("127.0.0.1", 8888)


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    while True:
        word = input("输入单词：")
        if not word:
            break
        udp_socket.sendto(word.encode(), server_address)
        data, addr = udp_socket.recvfrom(1024)
        print(data.decode())
    udp_socket.close()


main()
