<h1 align="center">📡 Chat Application using Python Sockets and PyQt5/QtPy</h1>

<p align="center">
    This is a <strong>real-time chat application</strong> built using <strong>Python sockets</strong> for communication between a client and a server. 
    The client interface is designed with <strong>PyQt5/QtPy</strong>, providing an intuitive and responsive GUI for sending and receiving messages.
</p>

<hr>

<h2>📚 Features</h2>
<ul>
    <li><strong>Real-time Communication:</strong> Seamless exchange of messages between client and server.</li>
    <li><strong>Graphical Interface:</strong> User-friendly chat interface with an elegant gradient background.</li>
    <li><strong>Custom UI Elements:</strong> Styled with PyQt5 and Qt Designer to enhance user experience.</li>
    <li><strong>Easy Configuration:</strong> Connects to <code>localhost:999</code> by default.</li>
</ul>

<hr>

<h2>🛠️ Technologies Used</h2>
<ul>
    <li><strong>Python 3.x</strong></li>
    <li><strong>Sockets</strong> (<code>socket</code> module)</li>
    <li><strong>PyQt5/QtPy</strong> (for GUI)</li>
</ul>

<hr>

<h2>📄 Code Overview</h2>

<h3>🖥️ Server Code (<code>server.py</code>)</h3>

```python
import socket

# Create a socket object
ser = socket.socket()

# Bind the server to localhost on port 999
ser.bind(('localhost', 999))

# Listen for incoming connections (max 3 clients)
ser.listen(3)

# Accept client connection
while True:
    c, address = ser.accept()
    print(' : ' + c.recv(1024).decode())
    
    # Handle message exchange between server and client
    while True:
        mes = input('::')
        c.send(bytes(mes, 'utf-8'))
        print(' ' + c.recv(1024).decode())

c.close()
