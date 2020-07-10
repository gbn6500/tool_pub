#!/usr/bin/python3

import sys
import os
import subprocess

args = sys.argv
argFile = args[1].split('.')
question = (argFile[0]).upper()
language =  argFile[1]

if language == "cpp":
    print('cpp')
    gccArgs = ['g++','-std=c++17','-o','a',args[1]]
    try:
        ret = subprocess.check_call(gccArgs)
    except:
        print(ret)
else:
    print('python')

homeDir = os.environ['HOME'] + '/'
path = homeDir + "dev/abc/testcase/"

cwd = os.path.basename(os.getcwd())
path += 'abc' + cwd[:3] + "/"
path += question + "/"
inPath = path + "in/"
outPath = path + "out/"

inFiles = os.listdir(inPath)
inFiles.sort()

AC = 0
WA = 0

for f in inFiles:
    inFile = inPath + f
    inStr=['','a']
    inStr[0] = 'cat {0}'.format(inFile)

    if language == "py":
        inStr[1] = "python3 {0}".format(args[1])


    pIn_pre = subprocess.Popen(inStr[0].split(" "),stdout=subprocess.PIPE)
    pIn_post = subprocess.Popen(inStr[1].split(" "),stdin=pIn_pre.stdout,stdout=subprocess.PIPE)
    pIn = pIn_post.communicate()
    myAnswer = pIn[0].decode()

    outFile = outPath + f
    of = open(outFile)
    correctAns = of.read()
    of.close()

    if myAnswer == correctAns:
        AC += 1
    else:
        WA += 1
        print('{0}: \n自分の答え [{1}] \n正解 [{2}]'.format(f,myAnswer[:-1],correctAns[:-1]))

print('{0} x AC'.format(AC))
print('{0} x WA'.format(WA))
