# AppiumDemo


## 获取 app 信息

获取当前界面元素：`adb shell dumpsys activity top`

获取任务列表：`adb shell dumpsys activity activities`
app入口：`adb logcat |grep -i displayed` 
`apkanalyzer` 最新版本的sdk中才有

启动应用：`adb shell am start -W -n xxx -S`

安装应用：`adb install -r xxx`