import socket

sock = socket.socket()
sock.bind(('',9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg=''
while True:
    data = conn.recv(1024)
    if not dara:
        break
    msg += data.decode()
    conn.send(data)

print(msg)

conn.close()
