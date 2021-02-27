import socket

HOST = "0.0.0.0" 
PORT = 65432

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

conn, addr = s.accept()
with conn:
    print("Connected by", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received from Client: " , data)
        if(data and data.decode()):
        	abc=data.decode()
        	#print("abc: ", abc)
        	try:
        		#x=eval(data.decode())
        		x=str(data.decode())
        		print(x)
        		y=x.split('\n')
        		print(y)
        	except Exception as e:
        		print(e)
        response='''HTTP/1.0 200 OK
Date: Sat, 27 Feb 2021 11:09:16 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2021-02-27-11; expires=Mon, 29-Mar-2021 11:09:16 GMT; path=/; domain=.localhost; Secure
Set-Cookie: NID=210=WbRHbahEEHAWwFcFxELCcx9gXzvobTchhMIdnKFKnAyVLustxLsi-2CBjcYjR-p_4FkOkVdOV8YtYHjE2U5NjN1s0cIlK08CUbzAAN5L7trsAGKs2-taVmHlY8cVwW65Gve7WpRRsfjEgAyiXq_2V3ZGC8a0KsFTJgkMB7LOecM; expires=Sun, 29-Aug-2021 11:09:16 GMT; path=/; domain=.localhost; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding

{ "hi": "hello" }
        '''
        conn.sendall(response.encode())
s.close()