#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        testCase.py
#
# Purpose:     This module is a test case module used as and example and test 
#              the function of the module <webScreenShoter.py>
#              
# Author:      Yuancheng Liu
#
# Created:     2024/05/03
# Version:     v_0.1.2
# Copyright:   Copyright (c) 2024 LiuYuancheng
# License:     MIT License 
#-----------------------------------------------------------------------------

import os
import webScreenShoter
from webScreenShoter import QT_DRIVER, CH_DRIVER

MODE = QT_DRIVER

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def testCase():
    print("Current working directory is : %s" % os.getcwd())
    dirpath = os.path.dirname(os.path.abspath(__file__))
    print("Current source code location : %s" % dirpath)
    capturer = webScreenShoter.webScreenShoter()
    urlListFile = "urlList.txt"
    urlListPath = os.path.join(dirpath, urlListFile)
    outputFolder = os.path.join(dirpath, "outputFolder")
    print("> load url record file %s" % urlListPath)
    urlList = []
    with open(urlListPath) as fp:
        urllines = fp.readlines()
        for line in urllines:
            if line[0] in ['#', '', '\n', '\r', '\t']: continue  # jump comments/empty lines.
            if ('http' in line):
                line = line.strip()
                urlList.append(line)
    capturer.getScreenShot(urlList, outputFolder, driverMode=MODE)

#-----------------------------------------------------------------------------
if __name__ == '__main__':
    testCase()