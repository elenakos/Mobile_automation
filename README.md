Steps to start Appium-python automation
1) Install node.js since appium is a web server written in Node.JS: brew install node
2) Install Appium: npm install -g appium
3) Install a web driver: npm install wd
4) Install android studio, it comes with an sdk - https://developer.android.com/studio/install.html
5) Add ANDROID_HOME to PATH
6) Install Appium python client https://github.com/appium/python-client
7) Connect a mobile device to your computer 

Open two terminal tabs:
1) Start appium int he first tab
2) Use it for adb commands or python

To find all devices attached to your computer:
adb devices -l

To find a package name for your Android application; in this case Calculator:
db shell 'pm list packages' | grep 'calcul'
package:com.google.android.calculator

To find an active application:
adb shell dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'
Reply:
  mCurrentFocus=Window{7f49c61 u0 com.google.android.calculator/com.android.calculator2.Calculator}
  mFocusedApp=AppWindowToken{7a594f1 token=Token{8e91e7b ActivityRecord{86e0675 u0 com.google.android.calculator/com.android.calculator2.Calculator t851}}}



