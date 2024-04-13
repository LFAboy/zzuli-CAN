import subprocess

# 点击zzuli-student 网络建立连接
def wifi_connect():
  network_name = "zzuli-student"
  command = f'/usr/sbin/networksetup -setairportnetwork en0 "{network_name}"'
  subprocess.run(command, shell=True)
  print(f"Connected to {network_name}")