import re

outputFileFinal = open("final_outputs_2.txt","a")
inputFile = open("outputs10.txt","r")
count = 0
for line in inputFile:
    if re.findall("\t\t",line):
        count = count + 1
        outputFileFinal.write(line)

print(f"{inputFile} pushed {count} lines in {outputFileFinal}")
outputFileFinal.close()
inputFile.close()
