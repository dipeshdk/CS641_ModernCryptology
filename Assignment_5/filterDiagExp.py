#Possible values of exponent vector
possibleExp = [[]*8]
#Possible values of matrix
possibleDiagMat = [[]*8]

#Possible values of exponent vector Filtered
possibleExpFiltered = [[]*8]
#Possible values of matrix Filtered
possibleDiagMatFiltered = [[]*8]
possibleOffDiag = [[]*7]

inputFile = open("inputs.txt", 'r')
outputFile = open("outputs.txt", 'r')

lineNo = 0
for (inpLine, outLine) in zip(inputFile.readlines(), outputFile.readlines()):
    #Since we are checking 2 bytes of output this time, last set discarded
    if lineNo > 6:
        break
    for mat in range(0, 128):
        for (exp_i, mat_i) in zip(possibleExp[lineNo], possibleDiagMat[lineNo]):
            for (exp_iplus, mat_iplus) in zip(possibleExp[lineNo+1], possibleDiagMat[lineNo+1]):
                valid = True
                for (inp, out) in zip(inpLine.strip.split(" "), outLine.strip.split(" ")):
                    inpBytes = block_to_byte(inp) #funcname
                    outBytes = block_to_byte(out)

                    EA_i = Multiply(mat_iplus, Exp(inpBytes[lineNo], exp_i))
                    EA_iplus = Multiply(mat, Exp(inpBytes[lineNo], exp_i))
                    EAEA_iplus = Add(Multiply(mat, Exp(EA_i, exp_i)), Multiply(mat_iplus, EXP(EA_iplus, exp_iplus)))
                    EAEAE_iplus = Exp(EAEA_iplus, exp_iplus)

                    if EAEAE_iplus != ord(outBytes[lineNo+1]):
                        valid = False

                if valid:
                    possibleExpFiltered[lineNo].append(exp_i)
                    possibleExpFiltered[lineNo+1].append(exp_iplus)
                    possibleDiagMatFiltered[lineNo].append(mat_i)
                    possibleDiagMatFiltered[lineNo+1].append(mat_iplus)
                    possibleOffDiag[lineNo].append(mat)
    lineNo = lineNo+1

print(possibleExpFiltered)
print(possibleDiagMatFiltered)
print(possibleOffDiag)
