Title: 工控安全工具集
Date: 2017-02-23 15:24
Tags: 工具

    本文所提到的相关部分工具具有攻击性，请务在真实环境中使用，否则后果自负。点击标题即可下载。

## 1、S7 Client Demo
开源的S7协议库”snap7“基础上进行开发的，主要支持西门子的S7-300/s7-400设备，可以直接连接西门子的控制器，获取控制器上的设备信息（如固件版本，块信息等），还可以直接操作控制器的CPU的启停。[下载地址](https://github.com/w3h/icsmaster/tree/master/tool/s7clientdemo.rar)
![Alt text](/static/images/icstools/1.gif =100*100)

## 2、PLCSCAN
通过探测设备，获取关于设备的供应商类型、模块信息等，目前仅支持S7协议与MODBUS协议。[下载地址](https://github.com/w3h/icsmaster/tree/master/tool/plcscan.rar)
![Alt text](/static/images/icstools/2.gif =100*100)

## 3、QTester104
使用QT和C++实现IEC104通讯规约，可以连接IEC104的设备。[下载地址](https://github.com/w3h/icsmaster/tree/master/tool/qtester104-v1.18.zip)
![Alt text](/static/images/icstools/3.gif)

## 4、S7-Brute-Offline
S7密码离线暴力破解工具。[下载地址](https://github.com/w3h/icsmaster/tree/master/tool/s7-brute-offline.py)
![Alt text](/static/images/icstools/4.gif)

## 5、SCADA_Metasploit_Modules
列举了MSF上所有的针对工业控制系统的漏洞脚本。[下载地址](https://github.com/w3h/icsmaster/tree/master/SCADA_Metasploit_Modules.csv)
![Alt text](/static/images/icstools/5.gif)

## 6、Scada_Password
列举了工业控制系统中的常见的用户和密码。[下载地址](https://github.com/w3h/icsmaster/tree/master/Scada_Password.csv)
![Alt text](/static/images/icstools/6.gif)

## 7、Scada_Dorks
收集针对工业控制系统中常见的DORK。[下载地址](https://github.com/w3h/icsmaster/tree/master/Scada_Dorks.csv)
![Alt text](/static/images/icstools/7.gif)

## 8、Scapy
Scapy的是一个强大的交互式数据包处理程序（使用python编写）。它能够伪造或者解码大量的网络协议数据包，能够发送、捕捉、匹配请求和回复包等等。它可以很容易地处理一些典型操作，比如端口扫描，tracerouting，探测，单元测试，攻击或网络发现（可替代hping，NMAP，arpspoof，ARP-SK，arping，tcpdump，tethereal，P0F等）。最重要的他还有很多更优秀的特性——发送无效数据帧、注入修改的802.11数据帧、在WEP上解码加密通道（VOIP）、ARP缓存攻击（VLAN）等，这也是其他工具无法处理完成的。
该工具主要用于工控协议解析，常用协议攻击（如tcp_land、arp fload等），工控协议FUZZ测试和漏洞利用脚本的编写。[下载地址](https://github.com/secdev/scapy.git)

