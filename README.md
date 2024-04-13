# ZZULI CAN(Campus Area Network) Login Automatically
自动登录郑州轻工业大学校园网脚本

#### Background

Mac OS 系统由于 CNA(Captive Network Assistant).app 的存在，导致每次CAN验证都是使用一个弹窗打开，且在这个弹窗中用不了密码填充，只能老老实实输一遍账号密码，选择运营商。2024.4.10号早上开电脑的时候又弹窗了验证，受不了了，就开始搞这个脚本。到11号解决了脚本登录问题，12号解决了 CNA.app的弹窗，期间参考了好多文档（参考<a href="#more">More</a>），也推倒重来了几遍，终于写出了一个适配的脚本了。

## Intro
这个仓库是一个自动登录zzuli CAN 的脚本，节省了密码认证环节。
只需要启动这个脚本就可以换成网络认证。

### Mac 连接公共网络的过程

1. 连接公共网络后，CNA.app 会自动检测网络是否通畅，如果不通会自动弹出一个页面，让用户去登录。
1. CNA.app 是通过 发送一个http/1.0的请求到 http://www.apple.com/library/test/success.html，根据回应判断是否通畅。
1. 如果回应跟它预计到结果一致，那么认为网络是通畅的，就不会自动弹出认证页面，流程结束。否则会弹出认证页面。
1. 如果回应中的html文件中的title 标签内容是 Success （大小写敏感）那么就认为是通畅的，否则就不通畅。

### 解决CNA.app 弹窗的原理&步骤

1. 改变 CNA.app 检测网络是否通畅的http 请求的URL ，指向一个返回含有 Success title 的地址即可。

2. 创建一个文件在 /Library/Preferences/SystemConfiguration/CaptiveNetworkSupport/Settings.plist，其中 Settings.plist 就是我们要创建的文件。这个文件指定了http检测请求的地址

3. 编辑Settings.plist 文件，内容如下：

   ```html
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList.dtd">
   <plist version="1.0">
   <dict>
     <key>CaptiveNetworkSupportVersion</key>
     <string>1.0</string>
     <key>ProbeURL</key>
     <string>http://captive.apple.com/hotspot-detect.html</string>
     <key>CaptivePortalSubdomains</key>
     <array>
       <string>apple.com</string>
       <string>example.com</string>
     </array>
     <key>HotspotProviders</key>
     <dict>
       <key>Apple</key>
       <dict>
         <key>ProbeURL</key>
         <string>http://captive.apple.com/hotspot-detect.html</string>
       </dict>
       <key>Example</key>
       <dict>
         <key>ProbeURL</key>
         <string>http://example.com/hotspot-detect.html</string>
       </dict>
     </dict>
   </dict>
   </plist>
   ```

4. 现在再次连接校园网就不会有弹窗了，不过此时并不能正常上网，认证弹窗会在浏览器中打开，我们可以选择用浏览器的密码填充工具，也可以用脚本发起一个http请求模拟我们的操作。

## Note

* 这个脚本目前只支持 Mac OS ，且保存在macos分支上，未来会更新 Win 平台保存在win分支，更新Android 平台在android 分支上。
* 当我们完成脚本后，断开校园网，<span style="color:red">关闭代理</span>，注意如果认证窗口在浏览器中打开了也不要通过浏览器认证，执行我们的脚本(python3 main.py), 看是否能连接上，如果连接上了，我们只需要把这个仓库打包成一个可执行文件，下次直接运行可执行文件就能连接校园网了。
* 本仓库中不包含如何打包成可执行文件的教程，请自行查阅。在<a href="#more">More</a> 中我也会给出我参考的一些比较有价值的博客，稍微折腾一下就可以了。

## <a id="more">More</a>

* **[手把手教你用Python实现自动连接校园wifi，附代码！]([手把手教你用Python实现自动连接校园wifi，附代码！ - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/530081384))**
* **[自动登录校园网脚本(Python实现)]([自动登录校园网脚本(Python实现) - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/370801224))**
* **[校园网自动登录全平台解决方案]([校园网自动登录全平台解决方案 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/364016452))**
* **[如何关闭Captive Network Assistant（CNA）自动弹出页面]([如何关闭Captive Network Ass… - Apple 社区](https://discussionschinese.apple.com/thread/44410?sortBy=best))**
* **[An undocumented change to Captive Network Assistant settings in OS X 10.10 Yosemite]([An undocumented change to Captive Network Assistant settings in OS X 10.10 Yosemite (grahamrpugh.com)](https://grahamrpugh.com/2014/10/29/undocumented-change-to-captive-network-assistant-settings-in-yosemite.html))**
* **[How to automatically login to captive portals on OS X?](https://apple.stackexchange.com/questions/45418/how-to-automatically-login-to-captive-portals-on-os-x)**
* **[What Is Apple Captive Network Assistant?]([What Is Apple Captive Network Assistant? (securew2.com)](https://www.securew2.com/blog/what-is-apple-captive-network-assistant))**
