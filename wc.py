# -*- coding: utf-8 -*-
# Author: Jiacheng Li
# Date: 7/10/2018
import sys

flag = False
lflag = False
wflag = False
cflag = False
args = sys.argv[1:]
count = 0
for arg in args:
    if arg == '-l' or arg == '-w' or arg == '-c':
        if arg == '-l':
            lflag = True
        if arg == '-w':
            wflag = True
        if arg == '-c':
            cflag = True
        flag = True
        count += 1
    elif arg == '-lw' or arg == '-wl':
        wflag = True
        lflag = True
        flag = True
        count += 1
    elif arg == '-wc' or arg == '-cw':
        wflag = True
        cflag = True
        flag = True
        count += 1
    elif arg == '-lc' or arg == '-cl':
        lflag = True
        cflag = True
        flag = True
        count += 1
    elif arg == '-lwc' or arg == '-wcl' or arg == '-clw' or arg == '-lcw' or arg == '-wlc' or arg == '-cwl':
        lflag = True
        wflag = True
        cflag = True
        flag = True
        count += 1
    else:
        isFlag = False
        if arg[0] == '-':
            isFlag = True
            if len(arg) == '1':
                break
        else:
            break

        for letter in arg[1:]:
            if not isFlag:
                if letter == '-':
                    isFlag = True
                else:
                    break

            if isFlag:
                if letter == 'l':
                    lflag = True
                elif letter == 'w':
                    wflag = True
                elif letter == 'c':
                    cflag = True
                else:
                    sys.exit('wc: illegal option -- %s\nusage: wc [-clmw] [file ...]' % letter)
        count += 1


# print(lflag, wflag, cflag)
# print(flag)
# print(args[count])

result = ''
filename = args[count:len(args)]
totalline = 0
totalword = 0
totalchar = 0
remain = filename.__len__()
for file in filename:
    try:
        with open(file) as f:
            linecount = f.read().count('\n')
            totalline += linecount
            f.close()
        with open(file) as f:
            charcount = len(f.read())
            totalchar += charcount
            f.close()
        with open(file) as f:
            wordcount = len(f.read().split())
            totalword += wordcount
            f.close()
        if flag:
            if lflag:
                # print('l')
                # print(linecount)
                result += ('\t%(linecount)s' % {'linecount': linecount})
            if wflag:
                # print('w')
                # print(wordcount)
                result += ('\t%(wordcount)s' % {'wordcount': wordcount})
            if cflag:
                # print('c')
                # print(charcount)
                result += ('\t%(charcount)s' % {'charcount': charcount})
            result += '\t'
            result += args[count]
        else:
            # print(args[count])
            result += ('\t%(linecount)s\t%(wordcount)s\t%(charcount)s\t' % locals())
            result += args[count]
        count += 1
        # print(remain)
        if remain > 1:
            result += '\n'

    except IOError as e:
        result += ('wc: %s: open: No such file or directory' % args[count])
        count += 1
        if remain > 1:
            result += '\n'
if remain > 1:
    if flag:
        if lflag:
            # print('l')
            # print(linecount)
            result += ('\t%(totalline)s' % {'totalline': totalline})
        if wflag:
            # print('w')
            # print(wordcount)
            result += ('\t%(totalword)s' % {'totalword': totalword})
        if cflag:
            # print('c')
            # print(charcount)
            result += ('\t%(totalchar)s' % {'totalchar': totalchar})
        result += '\ttotal'
    else:
        # print(args[count])
        result += ('\t%(totalline)s\t%(totalword)s\t%(totalchar)s\ttotal' % locals())

if remain == 0:
    print('wc:  : open: No such file or directory')

if not result == '':
    print(result)
