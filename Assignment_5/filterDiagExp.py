import req_functions as rf
#Possible values of exponent vector
possibleExp = [[20, 108], [20, 108], [22, 37, 68], [78, 85, 91], [18, 21, 88], [16, 50, 61], [23, 48, 56], [17, 41, 69]]
#Possible values of matrix
possibleDiagMat = [[84, 67], [77, 70], [33, 43, 98], [12, 8, 104], [64, 100, 112], [86, 11, 97], [27, 71, 92], [38, 61, 125]]

#Possible values of exponent vector Filtered
possibleExpFiltered = [[],[],[],[],[],[],[],[]]
#Possible values of matrix Filtered
possibleDiagMatFiltered = [[],[],[],[],[],[],[],[]]
possibleOffDiag = [[],[],[],[],[],[],[]]

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
                for (inp, out) in zip(inpLine.strip().split(" "), outLine.strip().split(" ")):
                    inpBytes = rf.block_to_byte(inp)
                    outBytes = rf.block_to_byte(out)
                    EA_i = rf.multiply_num(mat_i, rf.Exponential(ord(inpBytes[lineNo]), exp_i))
                    EA_iplus = rf.multiply_num(mat, rf.Exponential(ord(inpBytes[lineNo]), exp_i))
                    EAEA_iplus = rf.add_num(rf.multiply_num(mat, rf.Exponential(EA_i, exp_i)), rf.multiply_num(mat_iplus, rf.Exponential(EA_iplus, exp_iplus)))
                    EAEAE_iplus = rf.Exponential(EAEA_iplus, exp_iplus)

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
