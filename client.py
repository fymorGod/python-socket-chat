#client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = connect(('localhost', 8888))

ended = False 
print('Digite - tt - para terminar o chat')

while not ended:
  client.send(input('Mensagem: ').encode('utf-8'))
  msg = client.recv(1024).decode('utf-8')

  if msg == 'tt':
    endend = True
  else:
    print(msg)

client.close()