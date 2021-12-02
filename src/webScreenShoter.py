#!/usr/bin/python
#-----------------------------------------------------------------------------
# Name:        webScreenShoter.py
#
# Purpose:     This module will use different browser drivers API to capture the
#              webpage's screen shot img based on the given url. The user can also
#              use pyQT-5 QtWebEngineWidgets to download the whole web page by set
#              the related flag. The user can list all the urls he wants to download 
#              in the url file "urllist.txt" .
#
# Author:      Yuancheng Liu
#
# Created:     2021/11/23
# Version:     v_0.2
# Copyright:   n.a
# License:     n.a
#-----------------------------------------------------------------------------

import os
import sys
from time import sleep
from urllib.parse import urlparse
from selenium import webdriver

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt, QUrl, QTimer
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

GV_FLG = True  # Flag to identify whether use gloval value
if GV_FLG: import webGlobal as gv
URL_RCD = gv.URL_LIST if GV_FLG else 'urllist.txt'  # file to save url list
RST_DIR = gv.DATA_DIR if GV_FLG else 'datasets'
OUT_FILE = gv.SS_FILE_NAME if GV_FLG else 'shot.png'

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

class QTCapture(QWebEngineView):
    """ Capture the web page screen shot with QT5<QtWebEngineWidgets> driver."""
    # Reference link:
    # https://zetcode.com/pyqt/qwebengineview/
    # https://stackoverflow.com/questions/55231170/taking-a-screenshot-of-a-web-page-in-pyqt5
    # https://stackoverflow.com/questions/51154871/python-3-7-0-no-module-named-pyqt5-qtwebenginewidgets

    #-----------------------------------------------------------------------------
    def captureQT(self, url, outputDir):
        self.outputFile = os.path.join(RST_DIR, outputDir, OUT_FILE)
        self.load(QUrl(url))
        self.loadFinished.connect(self._onLoaded)
        # Create hidden view without scrollbars
        self.setAttribute(Qt.WA_DontShowOnScreen)
        self.page().settings().setAttribute(QWebEngineSettings.ShowScrollBars, False)
        self.show()

    #-----------------------------------------------------------------------------
    def _onLoaded(self):
        self.resize(self.page().contentsSize().toSize()) # Wait for resize
        QTimer.singleShot(1000, self._takeScreenshot)

    #-----------------------------------------------------------------------------
    def _takeScreenshot(self):
        self.grab().save(self.outputFile, b'PNG')
        self.app.quit()

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
class webScreenShoter(object):

    """ Download the webpage screen shot base on the input url."""
    def __init__(self, browserMD=False):
        self.browserMD = browserMD
        self.qtApp = None
        self.qtDriver = None
        if not self.browserMD: self.qtApp = QApplication(sys.argv)

    #-----------------------------------------------------------------------------
    def getScreenShot(self, url, folderName, browserMD=None):
        """ Init driver to capture the web screen shot based on the mode flag.
        Args:
            url ([str]): web url string.
            folderName ([string]): folder path to save the web components.
            browserMD ([bool], optional): User can reset the driver if he want to 
                change. True: Browser driver, False: QT5 driver. Defaults to None.
        Returns: [bool]: capture result.
        """
        if browserMD is bool: self.browserMD = browserMD
        if self.browserMD:
            self._captureBM(url, folderName)
        elif self.qtApp:
            self.qtDriver = QTCapture()
            self.qtDriver.app = self.qtApp
            self.qtDriver.captureQT(url, folderName)
            self.qtApp.exec_()
        else:
            print("> Error: the capture driver is not defined.")
            return False
        return True

    #-----------------------------------------------------------------------------
    def _captureBM(self, url, outputDir):
        """ Capture the url screen shot by browser driver.
        Args:
            url ([string]): web url string.
            outputDir ([string]): folder path to save the web components.
        """
        if sys.platform.startswith('win'):
            driverPath = gv.BROWSER_DRIVER_W if GV_FLG else "chromedriver.exe"
        else:
            driverPath = gv.BROWSER_DRIVER_L if GV_FLG else "chromedriver"
        driver = webdriver.Chrome(executable_path=driverPath)
        driver.get(url)
        sleep(1) # wait one second to let the browser to show the whole webpage
        if not os.path.exists(RST_DIR): os.mkdir(RST_DIR)
        filepath = os.path.join(RST_DIR, outputDir, OUT_FILE)
        #print("> path:"+filepath)
        driver.get_screenshot_as_file(filepath)
        driver.quit()
        driver = None
        #print("> Finished...")

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
def main():
    soup = webScreenShoter(browserMD=False)
    if not os.path.exists(RST_DIR):
        os.mkdir(RST_DIR)
    count = failCount = 0
    print("> load url record file %s" % URL_RCD)
    with open(URL_RCD) as fp:
        urllines = fp.readlines()
        for line in urllines:
            if line[0] in ['#', '', '\n', '\r', '\t']:
                continue  # jump comments/empty lines.
            count += 1
            print("> Process URL {}: {}".format(count, line.strip()))
            if ('http' in line):
                line = line.strip()
                domain = str(urlparse(line).netloc)
                folderName = "_".join((str(count), domain))
                filepath = os.path.join(RST_DIR, folderName)
                if not os.path.exists(filepath):
                    os.mkdir(filepath)
                result = soup.getScreenShot(line, folderName)
                #soup.savePage('https://www.google.com', 'www_google_com')
                if result:
                    print('> Finished.')
                else:
                    failCount += 1
    print("\n> Download result: download %s url, %s fail" %
          (str(count), str(failCount)))

#-----------------------------------------------------------------------------
if __name__ == '__main__':
    main()
