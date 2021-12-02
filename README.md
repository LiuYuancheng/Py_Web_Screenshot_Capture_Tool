# Web ScreenShoter

**Program Design Purpose**: We want to capture the screen shot images for several batch of webpages based on a list of URLs.



#### Introduction

This module will use different web browser's driver or Qt5 lib QtWebEngineWidgets to capture the part or the whole webpage's screen shot based on the given URL. The user can select the related lib he want to use to capture the webpage during the object init by passing in the "type" parameter. 

To prosses multiple URLs at the same time, The user can list all the url he wants to download  in the file "urllist.txt" as shown below: 

```
# Add the URL you want to download line by line(The url must start with 'http' or 'https' ):
# example: https://www.google.com
https://www.google.com
https://www.carousell.sg/
https://www.google.com/search?q=github&sxsrf=AOaemvJh3t5_h8H85AE8Ajbb1IMnBrRISA%3A1636698503535&source=hp&ei=hwmOYY6mHdGkqtsPq8S9sAY&iflsig=ALs-wAMAAAAAYY4Xl7GLWS16_xc2Q9XrG0p3q277DpkL&oq=&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzINCC4QxwEQowIQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJzIHCCMQ6gIQJ1AAWABgjgdoAXAAeACAAQCIAQCSAQCYAQCwAQo&sclient=gws-wiz
https://stackoverflow.com/questions/66022042/how-to-let-kubernetes-pod-run-a-local-script/66025424
```

###### Program Workflow

![](doc/img/screenshoter.png )

Version: v_0.2



------

#### Program Setup

###### Development Environment : python 3.7.4

###### Additional Lib/Software Need

1. **selenium**

   install: https://selenium-python.readthedocs.io/

   ```
   pip install selenium
   ```

2. **pyQT5** and **pyQT5-PyQtWebEngine**

   ```
   pip install PyQt5
   pip install PyQtWebEngine
   ```

   link: https://zetcode.com/pyqt/qwebengineview/

3. **Chrome browser driver**( optional, this lib need to work with selenium and fit your computer's browser version)

   link: https://chromedriver.chromium.org/downloads

4. 

###### Hardware Needed : None

###### Program Files List 

version: v0.2

| Program File       | Execution Env | Description                                  |
| ------------------ | ------------- | -------------------------------------------- |
| webScreenShoter.py | python 3      | Main executable program use the capture API. |
| urllist.txt        |               | url record list.                             |



------

#### Program Usage

###### Module API Usage

1. WebScreenShoter  Initialization : 

```
obj = webScreenShoter(browserMD=False)
```

- **browserMD**: Set to "True" to capture the web screenshot by using browser driver this need the computer with display output and installed the google-chrome browser , set to "False" to capture the web screen shot with pyQT5-webEngine. Default value is False.

2. Call API method "getScreenShot()"  to capture the screen shot of the webpage.

   ```
   obj.getScreenShot('<url>', '<folder_name>')
   
   # Exampe:
   obj.getScreenShot('https://www.google.com', 'www_google_com')
   ```

3.  Check the result: The web screen shot will be saved as file "shot.png" in the folder you set in the function "getScreenShot()". If the user use browser driver to capture, the resolution of shot.png will be a 1000x1000, else  whole page will be saved if QT5-webengine is used for capture.

4. --



###### Program Execution 

1. Copy the urls you want to check in the url record file "**urllist.txt**"

2. Cd to the program folder and run program execution cmd: 

   ```
   python webScreenShoter.py
   ```

3. Check the result: 

   For example, if you copy the url "https://www.carousell.sg/" as the first url you want to check into the file "urllist.txt" file, the screenshot file **shot.png** will be save under folder "1_www.carousell.sg_files"



------

#### Problem and Solution

###### Problem: Fail to capture url screen shot under browser mode

**OS Platform** : Windows

**Error Message**: Driver version too old ...

**Type**: Setup exception

**Solution**:

1.Make sure the computer is connected to a screen and google-chrome browser is installed. 

2.Browser driver not match browser version, web response timeout, web browser blocks the risky webpage. Download the corrected version of driver from the driver download link. 

**Related Reference**:  https://chromedriver.chromium.org/downloads



------

#### Reference 

- https://zetcode.com/pyqt/qwebengineview/
- https://stackoverflow.com/questions/55231170/taking-a-screenshot-of-a-web-page-in-pyqt5
- https://stackoverflow.com/questions/51154871/python-3-7-0-no-module-named-pyqt5-qtwebenginewidgets



------

> Last edit by LiuYuancheng(liu_yuan_cheng@hotmail.com) at 02/12/2021

