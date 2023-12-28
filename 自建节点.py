新机到手后先看IP是否正常：
https://www.toolsdaquan.com/ipcheck

Ping端口是否接通：
检测端口是否被封
端口被封的原因是多方面的，目前并没有哪一种节点可以保证不被封，本期讲的这三种方式也不例外，所以如果你的节点突然无法使用了，可以用以下方式进行排查。

打开 ping.pe

输入 IP 检测 ping 可用

输入 IP:Port 检查端口是否可用

主要是看最后几个是否为绿色



新机到手必做的10件事？让VPS飞速运行更安全！
Debian/Ubuntu安装下载工具

apt update -y  && apt install -y curl

官网版一键脚本

curl -sS -O https://kejilion.pro/kejilion.sh && chmod +x kejilion.sh && ./kejilion.sh


GitHub版一键脚本 部分小伙伴会遇到官网版出现大段乱码！就用GitHub版本吧！

curl -sS -O https://raw.githubusercontent.com/kejilion/sh/main/kejilion.sh && chmod +x kejilion.sh && ./kejilion.sh

1. DD系统
2. 更新系统
3. 清理系统
4. 修改密码 
5. 更换SSH端口 
6. 开放端口
7. 优化DNS地址 
8. 开启BBR3 
9. 修改时区
10. 添加虚拟内存大小


第一种搭建方法：搭建x-ui面板搭建节点
1、必要更新操作(Debian/Ubuntu)
apt update -y && apt install -y curl socat wget
**注意：**如果是centos系统，则分别运行yum update -y和yum install -y curl socat wget

2、安装x-ui
感谢github FranzKafkaYu大佬开发如此好用的一键脚本：

bash <(curl -Ls https://raw.githubusercontent.com/FranzKafkaYu/x-ui/master/install.sh)

X-ui 管理面板设置
添加证书和密钥路径，重启面板 通过域名访问x-ui 管理面板：https://域名:54321
注意事项：如果你点了 X-ui 面板设置，第一次进入的时候会自动帮你更改网址路径，点击确认，会自动跳转到新网址，下次再进入面板就需要通过这个新网址才能进入， 建议将其保存为书签，防止忘记了。

3、放行端口
放行指令是一样的，只要将端口443为任意端口就可以了。
放行 443 端口
iptables -I INPUT -p tcp --dport 443 -j ACCEPT
放行 54321 端口
iptables -I INPUT -p tcp --dport 54321 -j ACCEPT
放行全部端口
ufw disable




第二种搭建方法：hysteria 2一键部署管理脚本：

wget -N --no-check-certificate https://raw.githubusercontent.com/flame1ce/hysteria2-install/main/hysteria2-install-main/hy2/hysteria.sh && bash hysteria.sh

如果输入安装命令后提示wget: command not found，那是因为服务器系统没有自带wget命令，安装一下wget。

CentOS系统安装curl命令：yum install -y wget

Debian/Ubuntu系统安装curl命令：apt-get install -y wget





第三种搭建方法：ArgoX for VPS 运行脚本:

bash <(wget -qO- https://raw.githubusercontent.com/fscarmen/argox/main/argox.sh)

Option 参数	Remark 备注
-c	Chinese 中文
-e	English 英文
-a	Argo on-off Argo 开关
-x	Xray on-off Xray 开关
-s	Change the Argo tunnel 更换 Argo 隧道
-f	Variable file，refer to REPO file "config" 参数文件，可参数项目的文件 config
-u	Uninstall 卸载
-n	Export Nodes list 显示节点信息
-v	Sync Argo Xray to the newest 同步 Argo Xray 到最新版本
-b	Upgrade kernel, turn on BBR, change Linux system 升级内核、安装BBR、DD脚本






