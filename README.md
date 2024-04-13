# ZZULI CAN(Campus Area Network) Login Automatically
自动登录郑州轻工业大学校园网脚本

#### Background

Mac OS 系统由于 CNA(Captive Network Assistant).app 的存在，导致每次CAN验证都是使用一个弹窗打开，且在这个弹窗中用不了密码填充，只能老老实实输一遍账号密码，选择运营商。2024.4.10号早上开电脑的时候又弹窗了验证，受不了了，就开始搞这个脚本。到11号解决了脚本登录问题，12号解决了 CNA.app的弹窗，期间参考了好多文档（参考More），也推倒重来了几遍，终于写出了一个适配的脚本了。

## Intro
这个仓库是一个自动登录zzuli CAN 的脚本，节省了密码认证环节。
只需要启动这个脚本就可以换成网络认证。

### Mac 连接公共网络的过程

1. 连接公共网络后，CNA.app 会自动检测网络是否通畅

## Note

* 这个脚本目前只支持 Mac OS ，且保存在macos分支上，未来会更新 Win 平台保存在win分支，更新Android 平台在android 分支上。
* 