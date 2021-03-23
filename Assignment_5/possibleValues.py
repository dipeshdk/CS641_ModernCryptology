
#Possible values of exponent vector
possibleExp = [[]*8]
#Possible values of matrix
possibleDiagMat = [[]*8]

inputFile = open("inputs.txt", 'r')
outputFile = open("outputs.txt", 'r')

lineNo = 0
for (inpLine, outLine) in zip(inputFile.readlines(), outputFile.readlines()):
    for exp in range(1, 127):
        for mat in range(0, 128):
            validPair = True

            for (inp, out) in zip(inpLine.strip.split(" "), outLine.strip.split(" ")):
                inpBytes = block_to_byte(inp) #funcname
                outBytes = block_to_byte(out)

                EA = Multiply(mat, Exp(inpBytes[lineNo], exp))
                EAEA = Multiply(mat, Exp(EA, exp))
                EAEAE = Exp(EAEA, exp)

                if EAEAE != ord(outBytes[lineNo]):
                    validPair = False

            if validPair:
                possibleExp[lineNo].append(exp)
                possibleDiagMat[lineNo].append(mat)
    lineNo = lineNo+1

print(possibleExp)
print(possibleDiagMat)