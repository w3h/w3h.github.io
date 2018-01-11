Title: 构建虚拟工控环境系列 - 罗克韦尔虚拟PLC
Date: 2017-09-11 14:36
Tags: 虚拟PLC,软PLC
Authors: feilt


##一、	概述

本篇主要介绍罗克韦尔虚拟PLC的搭建，使用的操作系统为Windows7 x86 Ultimate（DEEP_GHOST_WIN7_SP1_X86_V2015_06.iso），虚拟化软件为 VVMware Workstation 12 Pro，（AB）SoftLogix5800 21.00.00。

为了研究罗克韦尔（AB）的软PLC，前后花了一周半的时间，遇到过AB的软件版本太高，破解不掉，改用低版本，虚拟化不支持；遇到过软件都支持虚拟化，但是版本直接兼容性不好；遇到过虚拟机下软件可以正常运行，但是联网后，用RSLinx扫描不到；试过Windows XP SP3 professional、Windows 7 SP1 x86 Ultimate、Windows 7 SP1 x64 Ultimate；遇到过物理机下可以用RSLinx扫描到，但虚拟机下扫描不到……

建议用深度的Ghost镜像“DEEP_GHOST_WIN7_SP1_X86_V2015_06.iso”。


##二、SoftLogix5800版本 

经测试AB公司Studio 5000 PLC编程软件V20以上版本完全兼容各个虚拟化环境。并且从V19版本开始，AB公司在诸多大项目中开始实际应用虚拟化环境的解决方案。
本文测试的软件版本如下：
Studio 5000 Logix Designer Professional Edition：V21.00.00（CPR9 SR 5.1）
RSLinx Classic Lite：3.51.01 （CPR9 SR 5.1）
SoftLogix Classic Monitor	：V21.00.00（CPR9 SR 5.1）

##三、安装Ghost Win7虚拟机

1、运行虚拟机VMware Workstation，创建一个新的虚拟机。
2、选中我们创建好的windows7虚拟机，“编辑虚拟机设置”，选用“使用ISO映像文件”。然后在“高级”中选择“IDE”模式。

![Alt text](/static/images/AB_VPLC/1.png)

3、完成后运行虚拟机，然后，按6选择“PQ8.05 – 图形分区工具”

![Alt text](/static/images/AB_VPLC/2.png)

4、硬盘分区，根据个人需要和实际情况填写，完成后“确定”。

![Alt text](/static/images/AB_VPLC/3.png)

5、接着按同样的步骤建立“逻辑分割磁区”。建立完成后选定主分区，“设定为作用”。

![Alt text](/static/images/AB_VPLC/4.png)

6、然后点击“执行”。完成后点击“结束”，然后关闭虚拟机。

![Alt text](/static/images/AB_VPLC/5.png)

7、进入BIOS，按“Shift”和“+”将从CD-ROM Drive调整为第一启动项。

![Alt text](/static/images/AB_VPLC/6.png)

8、然后选择从“安装系统到硬盘第一分区”。如果启动不正常，请关闭虚拟机，查看第2步中的磁盘模式是否是“IDE”模式。

![Alt text](/static/images/AB_VPLC/7.png)

9、系统自动安装。

![Alt text](/static/images/AB_VPLC/8.png)


##四、安装Rockwell Studio 5000

1、将安装软件解压后，打开RSLogix5000的文件夹，双击“Setup.exe”。

![Alt text](/static/images/AB_VPLC/9.png)

2、“序列号”输入“2022007039”。其他可以根据自己需要填写。然后“下一步”。

![Alt text](/static/images/AB_VPLC/10.png)

3、出现下面的界面直接点击“安装”，也可以根据自己的需要，取消一些选项，如“在联机丛书”。

![Alt text](/static/images/AB_VPLC/11.png)

4、然后点击“同意所有”。

![Alt text](/static/images/AB_VPLC/12.png)

5、静静的等待安装，期间弹出窗口或选项，直接“确认”或“下一步”。安装完成后点击“完成”。

![Alt text](/static/images/AB_VPLC/13.png)

6、安装完成后，在开始菜单中可以找到如下图标。

![Alt text](/static/images/AB_VPLC/14.png)


##五、安装SoftLogix5800

1、解压软件后，打开文件夹，双击“Install.exe”。

![Alt text](/static/images/AB_VPLC/15.png)

2、点击“SoftLogix 5800 V21.00”。

![Alt text](/static/images/AB_VPLC/16.png)

3、期间出现界面，则点击“Next”，出现下面的画面，则点击“Yes”。

![Alt text](/static/images/AB_VPLC/17.png)

4、“User Name”、“Company Name”和“Serial Number”与安装Studio5000中的相同。然后点击“Next”。

![Alt text](/static/images/AB_VPLC/18.png)

5、出现下面的对话框，表示是否创建“SoftLogix”的桌面快捷方式。根据个人爱好选择。本文选择“是”。

![Alt text](/static/images/AB_VPLC/19.png)

6、完成后，点击“Finish”，然后点击“EXIT”。

![Alt text](/static/images/AB_VPLC/20.png)


##五、软件破解

要点：因为软件在运行，部分文件不让修改，建议在重启虚拟机，启动时按F8，进入“安全模式”，将文件复制到物理计算机后修改，然后用修改后的文件替换原来的文件。

1、在C:\Program Files\Common Files\Rockwell目录下找到“FTACommon.dll”文件。

![Alt text](/static/images/AB_VPLC/21.png)

2、复制到物理机，用“UltraEdit”或其他相似的软件打开。在位置40FB9处，用“30 90”替换“34 02”。

![Alt text](/static/images/AB_VPLC/22.png)

3、替换完成后，保存，然后将修改后的文件，复制到虚拟机原来的目录下，替换原文件。

![Alt text](/static/images/AB_VPLC/23.png)


4、同样的方法修改替换以下文件。
（1）、C:\Program Files\Rockwell Software\FactoryTalk Activation\flexsvr.exe，位置E4D0，用“33 C0 40 89 45 FC 48 C3”替换“55 8B EC 83 E4 F8 81 EC”。
（2）、C:\Program Files\Rockwell Software\Studio 5000\Launcher\ActivationInterop.dll，位置5C86，用“E9 2C 00 00 00 90”替换“0F 85 46 03 00 00”。
（3）、C:\Program Files\Rockwell Software\Studio 5000\Launcher\ftastub.dll，位置FCD，用“09 00”替换“40 03”。
（4）、C:\Program Files\Rockwell Software\Studio 5000\Logix Designer\CHS\v21\Bin\LogixDesigner.exe，位置1DFB36，用“E9 2C 00 00 00 90”替换“0F 85 46 03 00 00”。
（5）、C:\Program Files\Rockwell Software\Studio 5000\Logix Designer\CHS\v21\Bin\ftastub.dll，位置FCD，用“09 00”替换“40 03”。
（6）、C:\Program Files\Rockwell Software\RSLinx\RSLINX.EXE，位置D9092，用“E9 2C 00 00 00 90”替换“0F 85 44 03 00 00”。
（7）、C:\Program Files\Rockwell Software\RSLinx\ftastub.dll，位置FCD，用“09 00”替换“40 03”。

5、破解完成后，重启计算机。进入系统后，会发现SoftLogix 5800自动启动。并出现下面的窗口，这是因为不是正版的原因。点击确定即可，不影响正常使用。

![Alt text](/static/images/AB_VPLC/24.png)


##五、连接演示

以下测试用了2台电脑，运行SoftLogix5800的计算机叫A，编程的计算机叫B。
1、配置计算机IP

![Alt text](/static/images/AB_VPLC/26.png)

2、启动SoftLogix的RSLinx。右键单击0槽，在弹出的菜单中单击“Start RSLinx”。

![Alt text](/static/images/AB_VPLC/27.png)

3、添加CPU模块。右键单击1槽，然后单击“Create”。选择“1789……”，然后一直“Next”，直至完成。

![Alt text](/static/images/AB_VPLC/28.png)

4、同样的方法，添加以太网模块。注意，选择刚才配置的那个IP地址。

![Alt text](/static/images/AB_VPLC/29.png)

5、同样的方法，添加2个信号模块。
6、完成后如下

![Alt text](/static/images/AB_VPLC/30.png)

7、打开电脑B的RSLinx，添加以太网驱动。

![Alt text](/static/images/AB_VPLC/31.png)

8、完成后，RSLinx自动扫描，一段时间后可以扫描到SoftLogix5800.

![Alt text](/static/images/AB_VPLC/32.jpg)

![Alt text](/static/images/AB_VPLC/33.png)

9、studio5000中连接SoftLogix。

![Alt text](/static/images/AB_VPLC/35.png)

10、编程下载

![Alt text](/static/images/AB_VPLC/36.png)

11、连接演示。

![Alt text](/static/images/AB_VPLC/37.png)


至此虚拟机下安装使用软PLC Softlogix5800已经完成。如果想了解更多信息请参考《1789-IN001K-EN-P》和《1789UM002J-EN-P》。


##六、结束语

（1）软件破解方法来自网络，破解方法版权归发帖人所有。想了解更多信息请参考：http://bbs.e10000.cn/a/a.asp?B=305&ID=1352006。
（2）本文仅用于研究学习，使用过程中出现任何问题，盖不负责。如用于商业用途，请购买正版软件。



