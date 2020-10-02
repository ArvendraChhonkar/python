import socket

ser = socket.socket()
ser.bind(('localhost',999))

ser.listen(3)

while True:
    c,adress = ser.accept()
    print(' : '+c.recv(1024).decode())
    while True:
        mes = input('::')
        c.send(bytes(mes,'utf-8'))
        print(' '+ c.recv(1024).decode())

c.close()