import utils
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
                inpBytes = utils.block_to_byte(inp) 
                outBytes = utils.block_to_byte(out)

                EA = utils.multiply_num(mat, utils.Exponential(ord(inpBytes[lineNo]), exp))
                EAEA = utils.multiply_num(mat, utils.Exponential(EA, exp))
                EAEAE = utils.Exponential(EAEA, exp)

                if EAEAE != ord(outBytes[lineNo]):
                    validPair = False

            if validPair:
                possibleExp[lineNo].append(exp)
                possibleDiagMat[lineNo].append(mat)
    lineNo = lineNo+1

# print(possibleExp)
# print(possibleDiagMat)

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
                    inpBytes = utils.block_to_byte(inp)
                    outBytes = utils.block_to_byte(out)
                    EA_i = utils.multiply_num(mat_i, utils.Exponential(ord(inpBytes[lineNo]), exp_i))
                    EA_iplus = utils.multiply_num(mat, utils.Exponential(ord(inpBytes[lineNo]), exp_i))
                    EAEA_iplus = utils.add_num(utils.multiply_num(mat, utils.Exponential(EA_i, exp_i)), utils.multiply_num(mat_iplus, utils.Exponential(EA_iplus, exp_iplus)))
                    EAEAE_iplus = utils.Exponential(EAEA_iplus, exp_iplus)

                    if EAEAE_iplus != ord(outBytes[lineNo+1]):
                        valid = False

                if valid:
                    possibleExpFiltered[lineNo].append(exp_i)
                    possibleExpFiltered[lineNo+1].append(exp_iplus)
                    possibleDiagMatFiltered[lineNo].append(mat_i)
                    possibleDiagMatFiltered[lineNo+1].append(mat_iplus)
                    possibleOffDiag[lineNo].append(mat)
    lineNo = lineNo+1

# print(possibleExpFiltered)
# print(possibleDiagMatFiltered)
# print(possibleOffDiag)

possibleMat = [[[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []]]
possibleExponentList = [[], [], [], [], [], [], [], []]

for i in range(8):
    possibleMat[i][i].append(possibleDiagMatFiltered[i][0])
    possibleExponentList[i].append(possibleExpFiltered[i][0])
    if(i < 7):
        possibleMat[i][i+1].append(possibleOffDiag[i][0])

# print(possibleExponentList)
# print(possibleMat)

for index in range(6):
    #As we have already found element next to diagonal thus skipping two elements every time
    of = index + 2
    
    exponentList = [e[0] for e in possibleExponentList]
    linearTransformList = [[0 for i in range(8)] for j in range(8)]
    #We fill all the empty [] elements with 0
    for i in range(8):
        for j in range(8):
            linearTransformList[i][j] = 0 if len(possibleMat[i][j]) == 0 else possibleMat[i][j][0]
    inputFile = open("inputs.txt", 'r')
    outputFile = open("outputs.txt", 'r')
    for ind, (inputLine, outputLine) in enumerate(zip(inputFile.readlines(), outputFile.readlines())):
        if ind > (7-of):
            continue
        inputString = [utils.block_to_byte(blockText) for blockText in inputLine.strip().split(" ")]
        outputString = [utils.block_to_byte(blockText) for blockText in outputLine.strip().split(" ")]
        #We iterate over all possible values of ai,j to find which one satisfies EAEAE = Output
        for i in range(1, 128):
            linearTransformList[ind][ind+of] = i
            flag = True
            for inputBlock, outputBlock in zip(inputString, outputString):
                if utils.eaeae(inputBlock, linearTransformList, exponentList)[ind+of] != ord(outputBlock[ind+of]):
                    flag = False
                    break
            if flag:
                possibleMat[ind][ind+of] = [i]
    inputFile.close()
    outputFile.close()
#We fill all the empty [] elements with 0
finalLinearTransformList = [[0 for i in range(8)] for j in range(8)]
for i in range(8):
    for j in range(8):
        finalLinearTransformList[i][j] = 0 if len(possibleMat[i][j]) == 0 else possibleMat[i][j][0]

print(finalLinearTransformList)
print(exponentList)