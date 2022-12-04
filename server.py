#server

import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8888))

server.listen()
client, address = server.accept()

ended = False

while not ended:
  msg = client.recv(1024).decode('utf-8')
  if msg == 'tt':
    ended = True
  else:
    print(msg)
  client.send(input('Mensagem: ').encode('utf-8'))

client.close()
server.close()