<h1 align="center">📡 Chat Application using Python Sockets and PyQt5/QtPy</h1>

<p align="center">
    This is a <strong>real-time chat application</strong> built using <strong>Python sockets</strong> for communication between a client and a server. 
    The client interface is designed with <strong>PyQt5/QtPy</strong>, providing an intuitive and responsive GUI for sending and receiving messages.
</p>
<hr>
<p align="center">Youtube Video :- </p>
## 📹 Demo and programing Video
[![Watch the video](https://img.youtube.com/vi/zHUUTGQWjrM/hqdefault.jpg)](https://youtu.be/zHUUTGQWjrM?si=_7d4mSjhJZZwqSDE)

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
```
<br> <h3>🖥️ Client GUI Code (<code>client.py</code>)</h3>
```
import sys
import socket
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

# Create a socket object
soc = socket.socket()

# Connect to the server on localhost and port 999
soc.connect(('localhost', 999))

class myclass(QWidget):
    def __init__(self):
        super(myclass, self).__init__()
        
        # Load the UI file (form.ui)
        loadUi('form.ui', self)
        
        self.setWindowTitle('Chatting Application - Arvendra')
        
        # Connect the "Send" button to the message sending function
        self.pushButton.clicked.connect(self.onsendcl)
        
    def onsendcl(self):    
        # Send the message to the server
        soc.send(bytes(self.sendtext.text() + "\n", 'utf-8'))
        
        # Receive and display the server's response
        self.sendandrec.append(
            '\n' + 'you: ' + self.sendtext.text() + '\n' + soc.recv(1024).decode()
        )

# Initialize the application
app = QApplication(sys.argv)
widget = myclass()
widget.show()

# Execute the application
sys.exit(app.exec())
soc.close()
```
<br> <h3>🎨 UI Design (<code>form.ui</code>)</h3> <p>This file defines the layout and appearance of the client’s graphical interface.</p>
✅ <strong>UI Elements:</strong>

<ul> <li><code>QLabel</code> for title and author name.</li> <li><code>QLineEdit</code> for entering messages (<code>sendtext</code>).</li> <li><code>QPushButton</code> for sending messages (<code>pushButton</code>).</li> <li><code>QTextEdit</code> for displaying chat history (<code>sendandrec</code>).</li> </ul> <hr> <h2>🌈 GUI Preview</h2> <p> The client interface includes: <ul> <li>A gradient background.</li> <li>Styled buttons and labels.</li> <li>Modern and sleek interface with a clean layout.</li> </ul> </p> <hr> <h2>📋 File Structure</h2> <pre> /chat-application ├── /form.ui # Qt UI file for client interface ├── /server.py # Server-side code └── /client.py # Client-side GUI code </pre> <hr> <h2>🚀 Getting Started</h2> <h3>📦 Prerequisites</h3> <ol> <li>Install Python (>= 3.8) from <a href="https://www.python.org/downloads/">python.org</a>.</li> <li>Install required packages:</li> </ol>
```
pip install pyqt5
pip install qtpy
```
<hr> <h3>📡 Running the Application</h3> <h4>Run the Server</h4> <ol> <li>Open a terminal and navigate to the server directory.</li> <li>Run the server:</li> </ol>
```python server.py```
The server will listen for connections on <code>localhost:999</code>.

<br> <h4>Run the Client</h4> <ol> <li>Open another terminal and run the client GUI:</li> </ol>
```
python client.py
```
The GUI will open, allowing you to send and receive messages.

<hr> <h2>📋 Usage Instructions</h2> <ol> <li><strong>Start the server first:</strong> Run <code>server.py</code> to listen for connections.</li> <li><strong>Run the client:</strong> Open the GUI using <code>client.py</code> and connect to the server.</li> <li><strong>Send messages:</strong> Type your message in the input field and click the "Send" button.</li> <li><strong>Receive responses:</strong> Messages from the server will be displayed in the chat window.</li> </ol> <hr> <h2>📚 UI Layout Details</h2> <p> Here’s a breakdown of the <code>form.ui</code> file: <ul> <li><strong>Background Gradient:</strong> Custom gradient applied using <code>QLabel</code>.</li> <li><strong>Message Input:</strong> <code>QLineEdit</code> styled with a clean, modern look.</li> <li><strong>Send Button:</strong> Styled with a dark background and white text.</li> <li><strong>Chat History Area:</strong> <code>QTextEdit</code> displays a conversation log.</li> </ul> </p> <hr> <h2>📝 Future Enhancements</h2> <ul> <li>✅ Multi-client support using threading.</li> <li>✅ Add encryption for secure communication.</li> <li>✅ Enhance the UI with additional styles and icons.</li> <li>✅ Implement error handling for socket exceptions.</li> </ul> <hr> <h2>🤝 Contributing</h2> <p> Contributions are welcome! Feel free to fork the repository, submit a pull request, or suggest new features. </p> <hr> <h2>📧 Contact</h2> <p> For any inquiries or issues, feel free to reach out. </p> <hr> <h3 align="center">✅ <strong>Happy Coding!</strong> 😊</h3> ```
✅ Instructions to Use:

Create a new file named README.md.

Copy and paste the above HTML content into the file.

Save the file in the root directory of your project.

When you upload this README.md to your GitHub repository, it will render with perfect formatting and styles, making it look clean and professional! 🚀

Let me know if you need further assistance! 😎✨
