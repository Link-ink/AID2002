from socket import *
import pymysql


class Database:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="123456",
                                  database="dict",
                                  charset="utf8"
                                  )

        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def find_word(self, word):
        sql = "select mean from words where word = %s;"
        self.cur.execute(sql, [word])
        mean = self.cur.fetchone()
        return mean[0]


def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("127.0.0.1", 8888))
    db = Database()
    while True:
        try:
            data, addr = udp_socket.recvfrom(50)
            mean = db.find_word(data.decode())
            udp_socket.sendto(mean.encode(),addr)
        except KeyboardInterrupt:
            break
    db.close()
    udp_socket.close()
    print("服务结束")


main()