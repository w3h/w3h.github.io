Title: 工业控制系统ClearEnergy勒索软件攻击
Date: 2017-04-08 14:36
Tags: 勒索软件


##1、背景

今年2月份佐治亚理工学院电气和计算机工程学院的科学家们在有限的范围内模拟了一个概念勒索软件（LogicLocker），主要目的是使用勒索软件的攻击手法来攻击关键基础设施、SCADA和工业控制系统。（此研究前期跟踪过，[链接](http://icsmaster.com/news/Ransomware%20for%20Industrial%20Control%20Systems.html)）
这只是一个模拟测试，仅仅过了1个多月，针对可编程逻辑控制器（PLC）中梯形图逻辑图的勒索软件攻击已经成型，代号**ClearEnergy**。针对工控系统的勒索软件攻击发展之快，但防御措施的推进如此艰难和缓慢，真令人担忧啊。


##2、介绍

**ClearEnergy**，攻击主要对象是关键基础设施、SCADA和ICS系统，是勒索软件攻击的一种（勒索软件是一种恶意软件，它以强大的加密算法感染计算机并加密其内容，然后要求赎金来解密该数据。）。一旦在受害机器上执行ClearEnergy，它将搜索易受攻击的可编程逻辑控制器（PLC），以便从PLC抓取梯形图逻辑图，并尝试将其上传到远程服务器。最后，ClearEnergy将启动一个定时器，它将触发一个进程，在一小时后从所有PLC中擦除逻辑图，除非受害者为了取消定时器并停止攻击而支付赎金。

勒索软件ClearEnergy影响响范围非常大，设备包括Schneider Electric Unity系列PLC和2.6版及更高版本的Unity OS，还包括GE和Allen-Bradley（MicroLogix系列），这些产品也被发现易受勒索软件攻击的攻击。影响的企业包括核电厂和设备厂，水和废物设施，运输基础设施等。

![ALT](/static/images/clearenergy/ClearEnergy-banner.jpg)

ClearEnergy攻击主要使用漏洞CVE-2017-6032（SVE-82003203）和CVE-2017-6034（SVE-82003204），该漏洞是施耐德电气公司的UMAS协议中的严重的安全漏洞。 UMAS协议由于协议会话密钥设计不良，仅一个字节长度（256种可能性），导致攻击者轻松猜测会话密钥，甚至可以嗅探。使用会话密钥，攻击者能够完全控制控制器，读取控制器的程序并用恶意代码重写。勒索软件ClearEnergy影响了世界上最大的SCADA和工业控制系统制造商的大量PLC型号。这包括Schneider Electric Unity系列PLC和2.6版及更高版本的Unity OS，其他领先供应商的PLC型号包括GE和Allen-Bradley（MicroLogix系列），这些产品也被发现易受勒索软件攻击的破坏。

目前，施耐德电气已经证实，Modicon系列PLC产品容易受到CRITIFENCE提出的发现，并发布了重要的网络安全通知（SEVD-2017-065-01）。国土安全部（ICS-CERT）今天也发布了一项重要的通告。

##3、验证

施耐德电气使用的UMAS协议格式如下图所示：

![ALT](/static/images/clearenergy/modbus_protocol.gif)

通过我们工控安全实验室的实际环境（Sichneider Quantum系列）截取的数据包如下图所示，可以获取通信的Seesion是0xb8：

![ALT](/static/images/clearenergy/ssession.gif)

利用获取的Session通过任意一台电脑可以发送控制CPU启停的命令以及程序上下载（POC见参考[4] **（POC请勿在实际环境中测试，否则后果自负）**），如下图所示：

![ALT](/static/images/clearenergy/session_stop_cpu.jpg)

使用Session发送Stop数据包后控制器Cpu进入Stop状态，如下图所示：

![ALT](/static/images/clearenergy/stop.jpeg)


##4、参考

[1] ClearEnergy Critical Infrastructure, SCADA and Industrial Control Systems ransomware analysis based on Modicon Modbus Protocol / UMAS - Session Key (0-Day Vulnerabilities)  [链接](http://www.critifence.com/blog/clear_energy/index.php?download_report)
[2] ClearEnergy ransomware aim to destroy process automation logics in critical infrastructure, SCADA and industrial control systems. [链接](http://securityaffairs.co/wordpress/57731/malware/clearenergy-ransomware-scada.html)
[3] Cybersecurity Notification – Modicon Family of PLCs [链接](http://download.schneider-electric.com/files?p_enDocType=Technical+leaflet&p_File_Id=7046260565&p_File_Name=SEVD-2017-065-01+Modicon+PLC+Family.pdf&p_Reference=SEVD-2017-065-01)
[4] POC下载地址 [链接](https://github.com/w3h/icsmaster/blob/master/exploit/MODBUS_REMOTE_COMMAND_TOOL.py)


