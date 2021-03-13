import paramiko
from paramiko import SSHClient
import time
import codecs

host = "65.0.124.36"
port = 22
username = "student"
password = "caesar"
buffsize=4096
serverTime = 0.1

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port, username, password,allow_agent=False,look_for_keys=False)
print("connected")
time.sleep(2)
chan=ssh.invoke_shell()
chan.set_environment_variable("TERM", "SPRING")
time.sleep(2)


print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

chan.send("Codagami\n")
time.sleep(serverTime)
while not chan.recv_ready():
        print("--------------------------------- not ready")
print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

chan.send("coda@cdr3#gami\n")
time.sleep(serverTime)
while not chan.recv_ready():
        print("--------------------------------- not ready")
print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

chan.send("4\n")
time.sleep(serverTime)
while not chan.recv_ready():
        print("--------------------------------- not ready")
print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

chan.send("read\n")
time.sleep(serverTime)
while not chan.recv_ready():
        print("--------------------------------- not ready")
print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

outputFile = open("outputs_4_round.txt","w+")
inputFile = open("input_plain_text_4_round.txt","r")
i = 0
missed =set()
for x in inputFile:
    print ("iteration number = ", i)
    i = i + 1
    print("input = ", x)

    chan.send(x)
    time.sleep(serverTime)
    f = 1
    while not chan.recv_ready():
        if f :
            f = 0
            missed.add(i)
            print("--------------------------------- not ready")
    response = codecs.decode(chan.recv(buffsize),  'UTF-8')
    print(response)
    outputFile.write(response)
    
    chan.send("c")
    time.sleep(serverTime)

    f = 1
    while not chan.recv_ready():
        if f :
            f = 0
            missed.add(i)
            print("--------------------------------- not ready")
    response = codecs.decode(chan.recv(buffsize),  'UTF-8')
    print(response)
    outputFile.write(response)

print(missed)
print("list size = ", len(missed))
print("total pairs = ", i)
inputFile.close()
outputFile.close()
chan.close()