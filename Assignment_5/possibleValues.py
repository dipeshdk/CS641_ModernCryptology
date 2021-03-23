import req_functions as rf
#Possible values of exponent vector
possibleExp = [[],[],[],[],[],[],[],[]]
#Possible values of matrix
possibleDiagMat = [[],[],[],[],[],[],[],[]]

inputFile = open("inputs.txt", 'r')
outputFile = open("outputs.txt", 'r')

lineNo = 0
for (inpLine, outLine) in zip(inputFile.readlines(), outputFile.readlines()):
    if lineNo > 7:
        break
    for exp in range(1, 127):
        for mat in range(0, 128):
            validPair = True

            for (inp, out) in zip(inpLine.strip().split(" "), outLine.strip().split(" ")):
                inpBytes = rf.block_to_byte(inp) 
                outBytes = rf.block_to_byte(out)

                EA = rf.multiply_num(mat, rf.Exponential(ord(inpBytes[lineNo]), exp))
                EAEA = rf.multiply_num(mat, rf.Exponential(EA, exp))
                EAEAE = rf.Exponential(EAEA, exp)

                if EAEAE != ord(outBytes[lineNo]):
                    validPair = False

            if validPair:
                possibleExp[lineNo].append(exp)
                possibleDiagMat[lineNo].append(mat)
    lineNo = lineNo+1

print(possibleExp)
print(possibleDiagMat)