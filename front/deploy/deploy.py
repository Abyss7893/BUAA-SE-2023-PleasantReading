import subprocess
import sys
import paramiko  # 是py的第三方库，需要自己使用pip安装
import os
ret = subprocess.call("npm install", shell=True)
print(f"安装完毕,状态码为:{ret}")
if ret != 0:
    print("安装出错!请检查文件配置")
    sys.exit()

ret = subprocess.call("npm run build", shell=True)
print(f"打包完毕,状态码为:{ret}")
if ret != 0:
    print("打包出错!请检查文件配置")
    sys.exit()

ret = subprocess.call("cd dist && jar -cvf PleasantReading.war *", shell=True)
print(f"压缩完毕,状态码为:{ret}")
if ret != 0:
    print("压缩出错!")
    sys.exit()

trans = paramiko.Transport('154.8.183.51', 22)  # 此处为服务器ip和端口，可自行更改
trans.connect(username='ubuntu', password="###")
sftp = paramiko.SFTPClient.from_transport(trans)
path = os.path.abspath('.') + '\dist\PleasantReading.war'
print(f'传递文件绝对位置为{path}')
# 此处为服务器前端配置对应dist的位置
sftp.put(path, '/home/ubuntu/PleasantReading_SE_2023/PleasantReading.war')
trans.close()
print("传输完毕")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 链接服务器
ssh.connect(hostname='154.8.183.51', port=22,
            username='ubuntu', password="###")
command = "cd /home/ubuntu/PleasantReading_SE_2023/;sudo rm -rf PleasantFront; unzip PleasantReading.war -d PleasantFront;sudo rm -rf PleasantReading.war; sudo service nginx reload;sudo service nginx start;"
stdin, stdout, stderr = ssh.exec_command(command)
res = stdout.read()

if not res:
    res = stderr.read()
    print("部署失败，发生错误:")
    print(res.decode())
    sys.exit()
else:
    print("解压完毕，旧版本删除完毕,部署完成.")
ssh.close()

ret = subprocess.call("rmdir /s /q dist", shell=True)
print(f"删除本地dist文件完毕,状态码为:{ret}")
if ret != 0:
    print("删除出错!")
    sys.exit()
print("success!")