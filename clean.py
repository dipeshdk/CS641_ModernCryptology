import re
outputFile = open("final_outputs.txt","w")
inputFile = open("outputs.txt","r")
for line in inputFile:
    if re.findall("\t\t",line):
        outputFile.write(line)