import gevent
from gevent import monkey
monkey.patch_all()  # 执行插件,修改原有阻塞,需要导入socket之前执行
from socket import *


# 客户端处理函数
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()

# 创建套接字
s = socket()
s.bind(('0.0.0.0', 8888))
s.listen(5)

while True:
    c, addr = s.accept()
    print("Connect from", addr)
    # handle(c) # 循环方案
    gevent.spawn(handle, c)  # 协程方案
s.close()
