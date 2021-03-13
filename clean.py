import re

outputFileFinal = open("final_outputs_2.txt","w+")
inputFile = open("outputs.txt","r")
for line in inputFile:
    if re.findall("\t\t",line):
        outputFileFinal.write(line)

outputFileFinal.close()
inputFile.close()
