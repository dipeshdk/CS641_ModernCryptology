import numpy as np
import random
import sympy as sp
from numpy.linalg import matrix_rank
np.set_printoptions(threshold=np.inf)
from pyfinite import ffield
import req_functions as utils
import eaeae 

possibleMat=[[[84], [114], [], [], [], [], [], []], [[], [70], [17], [], [], [], [], []], [[], [], [43], [26], [], [], [], []], [[], [], [], [12], [104], [], [], []], [[], [], [], [], [112], [100], [], []], [[], [], [], [], [], [11], [92], []], [[], [], [], [], [], [], [27], [31]], [[], [], [], [], [], [], [], [38]]]
possibleExponentList=[[20], [108], [37], [78], [88], [50], [23], [17]]

for index in range(6):
    #As we have already found element next to diagonal thus skipping two elements every time
    of = index + 2
    
    exponentList = [e[0] for e in possibleExponentList]
    linearTransformList = [[0]*8]*8
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
                if eaeae.eaeae(inputBlock, linearTransformList, exponentList)[ind+of] != ord(outputBlock[ind+of]):
                    flag = False
                    break
            if flag:
                possibleMat[ind][ind+of] = [i]
    inputFile.close()
    outputFile.close()
#We fill all the empty [] elements with 0
finalLinearTransformList = [[0]*8]*8
for i in range(8):
    for j in range(8):
        finalLinearTransformList[i][j] = 0 if len(possibleMat[i][j]) == 0 else possibleMat[i][j][0]

print(finalLinearTransformList)
print(exponentList)