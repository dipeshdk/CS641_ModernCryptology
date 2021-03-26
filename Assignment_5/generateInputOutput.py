import numpy as np
import random
import sympy as sp
from numpy.linalg import matrix_rank
np.set_printoptions(threshold=np.inf)
import paramiko
from paramiko import SSHClient
import time
import codecs
import re
import os

#generate plaintext input
mapping = {}
for i in range(16):
    numInBinary = '{:0>4}'.format(format(i,"b"))
    numi = int(numInBinary[3]) + 2 *int(numInBinary[2]) + int(numInBinary[1]) * 4 + int(numInBinary[0])*8
    mapping[numInBinary] = chr(ord('f')+numi)

inputFile = open("inputs.txt","w+")
for i in range(8):
    for j in range(128):
        curr_ip_j = np.binary_repr(j, width=8)
        strr = 'ff'*i + mapping[curr_ip_j[:4]] + mapping[curr_ip_j[4:]] + 'ff'*(8-i-1)
        inputFile.write(strr)
        inputFile.write(" ")
    inputFile.write("\n")
inputFile.close()
# exit()

#fetch ciphertext
host = "65.0.124.36"
port = 22
username = "student"
password = "caesar"
buffsize=4096
serverTime = 0.5
sleepTime = 0.01

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

chan.send("5\n")
time.sleep(serverTime)
while not chan.recv_ready():
        print("--------------------------------- not ready")
print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

chan.send("go\n")
time.sleep(serverTime)
while not chan.recv_ready():
        print("--------------------------------- not ready")
print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

chan.send("wave\n")
time.sleep(serverTime)
while not chan.recv_ready():
        print("--------------------------------- not ready")
print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

chan.send("dive\n")
time.sleep(serverTime)
while not chan.recv_ready():
        print("--------------------------------- not ready")
print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

chan.send("go\n")
time.sleep(serverTime)
while not chan.recv_ready():
        print("--------------------------------- not ready")
print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

chan.send("read\n")
time.sleep(serverTime)
while not chan.recv_ready():
        print("--------------------------------- not ready")
print (codecs.decode(chan.recv(buffsize),  'UTF-8'))

outputFile = open("temp.txt","w+")
inputFile = open("inputs.txt","r")
i = 0
missed =set()
for line in inputFile:
    # if 1:
    for x in line.split(' '):
        if len(x) < 16:
            continue
        print ("iteration number = ", i)
        i = i + 1
        print("input = ", x)
        chan.send(x + '\n')
        time.sleep(sleepTime)
        f = 1
        while not chan.recv_ready():
            if f :
                f = 0
        while 1:
            if chan.recv_ready():
                response = codecs.decode(chan.recv(buffsize),  'UTF-8')
                print(response)
                outputFile.write(response)
                if len(response) > 1:
                    if response[-2] == '>':
                        break
        chan.send("c\n")
        time.sleep(sleepTime)
        f = 1
        while not chan.recv_ready():
            if f :
                f = 0
        while 1:
            if chan.recv_ready():
                response = codecs.decode(chan.recv(buffsize),  'UTF-8')
                print(response)
                outputFile.write(response)
                if len(response) > 1:
                    if response[-2] == '>':
                        break
        time.sleep(sleepTime)


inputFile.close()
outputFile.close()
chan.close()

#clean fetched output
outname = "outputs.txt"
inname = "temp.txt"
outputFileFinal = open(outname,"w+")
inputFile = open(inname,"r")

i = 0
for line in inputFile:
    if re.findall("\t\t",line):
        i = i + 1
        outputFileFinal.write(line.strip('\t\t').strip('\n') + ' ')
        if i % 128 == 0:
                outputFileFinal.write('\n')
outputFileFinal.close()
inputFile.close()
os.remove(inname)