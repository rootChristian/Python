#SERVER WEB
#!/usr/bin/env python
#coding:utf-8

import socket
import threadind

#=================================================================
class ThreadForClient(threading.Thread): #classe pour communiquer avec chaque client
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn

    def run(self):
        data = conn.recv(1024)  #recieved data send by client
        data = data.decode("utf-8")
        print(data)

#=================================================================        

host=''
port=8888

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #definire la socket en ipv4 et tcp
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #definire les options
s.bind((host, port)) #lier le host et le port
print ("Server is run...")

while 1:
    s.listen(5)
    conn, address=s.accept()
    print ("One client connected: ", address)

    my_thread = ThreadForClient(conn)
    my_thread.start()
    
conn.close()
s.close()
    

'''
s.listen(5) #accepter les connections
client,adresse=s.accept() #accepter un client
print ("Client connected: ",adresse)
while 1:
    sms_client = client.recv(1024)
    print ("Client -> ", sms_client)
    if sms_client.upper() == "END" or sms_client == "":
        break
    sms_serveur=input("Serveur -> ")
    client.send(sms_serveur)

client.close()
s.close()

client.close()
s.close()
'''
