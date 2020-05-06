import socket
import os
import random
# 创建soket对象
sk=socket.socket()
# 绑定端口 ip
sk.bind(('127.0.0.1',8000))

sk.listen()

def handleIndex(data):
    dirname=os.path.dirname(__file__)
    with open(os.path.join(dirname,'index.html'),'r',encoding='utf-8') as f:
        html=f.read()
        html=html.replace('{{data}}',str(data))
        return html

# 等待链接
while True:
    #建立连接
    (conn,addr) = sk.accept()
    #接收数据
    data=conn.recv(2048).decode('utf-8')
    url=data.split()[1]
    # 返回数据
    conn.send(b'HTTP/1.1 200 OK \r\nContent-Type: text/html;charset=utf-8\r\n\r\n')
    res=''
    if url=='/oumei':
        res='<h1>芜桐oumei</h1>'
    elif url=='/rihan':
        res='<h1>rihan</h1>'
    elif url=='/index':
        res=handleIndex(random.randint(0,100))
    else:
        res='<h1>%s</h1>' % url
    conn.send(res.encode('utf-8'))
    # 断开连接
    conn.close()