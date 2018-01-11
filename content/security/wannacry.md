Title: Wannacry(永恒之蓝)勒索蠕虫跟踪分析
Date: 2017-05-13 14:36
Tags: 工控安全
Authors: w3h

##一、事件跟踪

北京时间2017年5月12日晚间，一款名为Wannacry 的蠕虫勒索软件袭击全球网络，经研究发现这是不法分子通过改造之前泄露的NSA黑客武器库中“永恒之蓝”攻击程序发起的网络攻击事件。“永恒之蓝”通过扫描开放445文件共享端口的Windows电脑甚至是相关移动终端，无需用户进行任何操作，只要开机联网，不法分子就能在电脑和服务器中植入勒索软件、远程控制木马、虚拟货币挖矿机等一系列恶意程序。这被认为是迄今为止最巨大的勒索交费活动，影响到近百个国家上千家企业及公共组织。 该软件被认为是一种蠕虫变种（也被称为“Wannadecrypt0r”、“wannacryptor”或“ wcry”）。 像其他勒索软件的变种一样，WannaCry也阻止用户访问计算机或文件，要求用户需付费解锁。相关影响截图如下：

![Alt text](/static/images/wannacry/1.jpg)

工匠实验室是华创网安旗下的专注于工控安全领域的研究实验室，作为工控安全的守护者，紧急启动应急响应，对事件和病毒进行了相关分析，希望通过微薄之力对网络安全做出贡献。

##二、安全态势

全球感染态势图

![Alt text](/static/images/wannacry/21.jpg)

感染TOP 20的国家统计

![Alt text](/static/images/wannacry/22.png)

初略的统计国内可能存在威胁主机（不包括台湾、香港、澳门）的分布图如下：

![Alt text](/static/images/wannacry/23.gif)


##三、病毒样本分析

样本本身会释放之后需要调用的加密文件以及其它的:
加密密码: WNcry@2ol7

![Alt text](/static/images/wannacry/31.png)

文件本身包含的文件如下:

![Alt text](/static/images/wannacry/32.png)


当样本运行起来之后,会释放在如下目录:

![Alt text](/static/images/wannacry/33.png)

创建并以服务的方式运行:
"ImagePath=cmd.exe /c "C:\Intel\ykpgmdelqxu787\tasksche.exe"" in key HKEY_LOCAL_MACHINE\system\Curre ntControlSet\Services\ykpgmdelqxu787

![Alt text](/static/images/wannacry/34.png)

已注册表的形式创建mssecsvc2.0服务并启动:

![Alt text](/static/images/wannacry/35.png)

提权代码:
icacls . /grant Everyone:F /T /C /Q

![Alt text](/static/images/wannacry/36.png)


样本执行之后会访问www.iuqerfsodp9ifjaposdfjhgosurijfaewrwergwea.com通过 80端口,开始实现端口扫描并尝试连接:

![Alt text](/static/images/wannacry/37.png)


通过cmd启动tasksche.exe进程：
C:\Intel\ykpgmdelqxu787\tasksche.exe, C:\Intel\ykpgmdelqxu787\tasksche.exe, C:\WINDOWS\system32。

tasksche.exe会创建taskdl.exe,attrib.exe子进程调用cscript.exe进程实现加密 ：
C:\WINDOWS\system32\cscript.exe, cscript.exe //nologo m.vbs, C:\Intel\ykpgmdelqxu787

进程关系如下：

![Alt text](/static/images/wannacry/38.png)


加密扩展文件如下，可以看出加密的文件中并不是针对工控网络:

.der, .pfx, .key, .crt, .csr, .p12, .pem, .odt, .ott, .sxw, .stw, .uot, .3ds, .max, .3dm, .ods, .ots, .sxc, .stc, .dif, .slk, .wb2, .odp, .otp, .sxd, .std, .uop, .odg, .otg, .sxm, .mml, .lay, .lay6, .asc, .sqlite3, .sqlitedb, .sql, .accdb, .mdb, .db, .dbf, .odb, .frm, .myd, .myi, .ibd, .mdf, .ldf, .sln, .suo, .cs, .cpp, .pas, .asm, .js, .cmd, .bat, .ps1, .vbs, .vb, .pl, .dip, .dch, .sch, .brd, .jsp, .php, .asp, .rb, .java, .jar, .class, .sh, .mp3, .wav, .swf, .fla, .wmv, .mpg, .vob, .mpeg, .asf, .avi, .mov, .mp4, .3gp, .mkv, .3g2, .flv, .wma, .mid, .m3u, .m4u, .djvu, .svg, .ai, .psd, .nef, .tiff, .tif, .cgm, .raw, .gif, .png, .bmp, .jpg, .jpeg, .vcd, .iso, .backup, .zip, .rar, .7z, .gz, .tgz, .tar, .bak, .tbk, .bz2, .PAQ, .ARC, .aes, .gpg, .vmx, .vmdk, .vdi, .sldm, .sldx, .sti, .sxi, .602, .hwp, .snt, .onetoc2, .dwg, .pdf, .wk1, .wks, .123, .rtf, .csv, .txt, .vsdx, .vsd, .edb, .eml, .msg, .ost, .pst, .potm, .potx, .ppam, .ppsx, .ppsm, .pps, .pot, .pptm, .pptx, .ppt, .xltm, .xltx, .xlc, .xlm, .xlt, .xlw, .xlsb, .xlsm, .xlsx, .xls, .dotx, .dotm, .dot, .docm, .docb, .docx, .doc, .c, .h


##四、防御措施

为了减少网络攻击造成的影响，华创网安相关产品紧急更新了相关防护措施，监测审计产品，已经部署相关规则，可以及时发现网络中的蠕虫病毒。工控漏洞评估系统已增加相应的漏洞检测脚本，可以提前发现网络中的存在漏洞的主机。

####1、传统网络防护措施
根据此攻击，传统网络的防御措施如下：

1．防火墙屏蔽445端口
2．利用 Windows Update 进行系统更新
3．关闭 SMBv1 服务
4．部署相应的检测规则

【检测规则】
尽快部署在相关网络设备中部署如下检测规则

alert smb any any -> $HOME_NET any (msg:”ET EXPLOIT Possible ETERNALBLUE MS17-010 Echo Request (set)”; flow:to_server,established; content:”|00 00 00 31 ff|SMB|2b 00 00 00 00 18 07 c0|”; depth:16; fast_pattern; content:”|4a 6c 4a 6d 49 68 43 6c 42 73 72 00|”; distance:0; flowbits:set,ETPRO.ETERNALBLUE; flowbits:noalert; classtype:trojan-activity; sid:2024220; rev:1;)

alert smb $HOME_NET any -> any any (msg:”ET EXPLOIT Possible ETERNALBLUE MS17-010 Echo Response”; flow:from_server,established; content:”|00 00 00 31 ff|SMB|2b 00 00 00 00 98 07 c0|”; depth:16; fast_pattern; content:”|4a 6c 4a 6d 49 68 43 6c 42 73 72 00|”; distance:0; flowbits:isset,ETPRO.ETERNALBLUE; classtype:trojan-activity; sid:2024218; rev:1;)


【漏洞补丁】
由于本次Wannacry蠕虫事件的巨大影响，微软总部刚才决定发布已停服的XP和部分服务器版特别补丁。注意工控现场设备一定需要充分验证后才去更新相应的补丁。
https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/

![Alt text](/static/images/wannacry/41.png)


####2、工控网络防护措施

传统网络防御措施都适合工控网络吗，答案当然是否定的，原因如下：

1. 工控网络主机在安装相关软件时，会关闭windows防火墙，开启防火墙会影响上位机与控制设备之间的通信。

2. 更新windows补丁。连续性生产的设备上是无法实施，一旦因为补丁影响通信，后果无法估量。

3. 关闭SMBv1服务。连续性生产的设备上是无法实施。

4. 部署相应的检测规则。可以实施，尽快更新边界防护策略。

由此可见，工控网络对于网络安全事件的响应是多么的困难和缓慢。不过幸庆的是，目前此蠕虫病毒仅通过网络进行传播，还未发现感染移动介质，很多工控网络因为隔离，躲过了此次攻击。但随着中国的工业4.0、智能制造等项目的推进，越来越多的工控系统会连接互联网，会了提前预防，我们是时候行动机来啦。对于此种类型的攻击，我们推荐的防御措施如下：

    1. 工控网络与信息网之间部署工控防火墙，禁示SMB协议数据的传播。

    2. 主机安装白名单的工控防护软件，限制移动介质的使用、非法软件的安装、非法进程的运行，避免移动介质的感染。

    3. 工控网络中部署监测设备，实时监测蠕虫病毒，一旦发现立即上报告警，进行应急响应。





