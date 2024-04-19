import subprocess

# 点击zzuli-student 网络建立连接
def wifi_connect():
  network_name = "zzuli-student"
  # 注意 windows 用户需要使用下面注释的代码
  # command = f'netsh wlan connect name="{network_name}"'
  command = f'/usr/sbin/networksetup -setairportnetwork en0 "{network_name}"' 
  subprocess.run(command, shell=True)
  print(f"Connected to {network_name}")



# 对于不需要网络认证的 Wi-Fi，单用下面的脚本配置 Wi-Fi 名称和 密码就可以自动连接。
# import subprocess

# network_name = "Your_WiFi_SSID"  这里的 SSID 指的就是 Wi-Fi 名称。
# password = "Your_WiFi_Password"

# command = f'netsh wlan connect name="{network_name}" ssid="{network_name}" keyMaterial="{password}"'
# subprocess.run(command, shell=True)
# print(f"Connected to {network_name}")