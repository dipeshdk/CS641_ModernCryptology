import re

outputFileFinal = open("test.txt","w+")
inputFile = open("outputs13.txt","r")

for line in inputFile:
    if re.findall("\t\t",line):
        outputFileFinal.write(line.strip('\t\t'))

outputFileFinal.close()
inputFile.close()
