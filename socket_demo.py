# coding=utf-8
# Server side
import socket

# Address
HOST = ''
PORT = 8000

# Prepare HTTP response
text_content = '''
HTTP/1.x 200 OK  
Content-Type: text/html

<head>
    <title>WOW</title>
</head>
<html>
    <p>Wow, Python Server</p>
    <IMG src="test.jpg"/>
    <form name="input" action="/" method="post">
        First name:<input type="text" name="firstname"><br>
        <input type="submit" value="Submit">
    </form> 
</html>
'''

# Read picture, put into HTTP format
f = open('test.jpg', 'rb')
pic_content = '''
HTTP/1.x 200 OK  
Content-Type: image/jpg

'''
pic_content = pic_content + f.read()
f.close()

# Configure socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 说明socket使用的是IPv4(AF_INET)和TCP协议(SOCK_STREAM)
s.bind((HOST, PORT))

# infinite loop, server forever
while True:
    # 3: maximum number of requests waiting
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024)
    p = request.split(' ')
    method = p[0]
    src = p[1]

    # deal with GET method
    if method == 'GET':
        # ULR
        if src == '/test.jpg':
            content = pic_content
        else:
            content = text_content

        print 'Connected by', addr
        print 'Request is:', request
        conn.sendall(content)
        # if POST method request
    elif method == 'POST':
        form = request.split('\r\n')
        idx = form.index('')  # Find the empty line
        entry = form[idx:]  # Main content of the request

        value = entry[-1].split('=')[-1]
        conn.sendall(text_content + '\n <p>' + value + '</p>')
        ######
        # More operations, such as put the form into database
        # ...
        ######
    # close connection
    conn.close()

