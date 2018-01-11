Title: 构建虚拟工控环境系列 - 西门子虚拟PLC
Date: 2017-07-30 14:36
Tags: 虚拟PLC,软PLC
Authors: feilt


##一、	概述

跟随着工控安全一路走来，工控安全市场今年明显有相当大的改善，无论从政策还是客户需求，都在逐步扩大中。但是，搞工控安全研究的人员却寥寥无几。一方面工控安全是个跨学课的技术，需要了解多方面的知识，有比较高的技术上的门槛；另一方面，没有可以研究和学习的便利的环境。一般，搞这方面研究的公司或者个人，都会先购买一些硬件设备，搭建一个模拟环境，再做相应的安全研究，成本实在是太高。为了解决这个问题，我们做了一系列的相关的技术研究，通过构建一套虚拟的工业控制环境，从而降低了解和学习工控安全的门槛，推动相关人才的培养。

本篇主要介绍西门子虚拟PLC，使用的操作系统为Windows7 x86 Ultimate，虚拟化软件为 VMware Workstation 12 Pro，（SIEMENS）WinAC RTX 2010。


##二、	控制器虚拟化技术介绍

可编程控制器，即PLC。PLC的实现分为硬PLC和软PLC。 所谓硬PLC从严格意义上来说是由硬件或者一块专用的ASIC芯片来实现PLC指令的执行．而软PLC是用一些通用的CPU或者MCU来实现PLC指令的解释或者编译持行。

软件PLC（SoftPLC，也称为软逻辑SoftLogic）是一种基于基于PC机开发结构的控制系统，它具有硬PLC在功能、可靠性、速度、故障查找等方面的特点，利用软件技术可以将标准的工业PC转换成全功能的PLC过程控制器。软件PLC综合了计算机和PLC的开关量控制、模拟量控制、数学运算、数值处理、网络通信、PID调节等功能，通过一个多任务控制内核，提供强大的指令集、快速而准确的扫描周期、可靠的操作和可连接各种I/O系统的及网络的开放式结构。所以，软件PLC 提供了与硬PLC同样的功能，同时又提供了PC环境的各种优点。

虚拟机技术是虚拟化技术的一种，所谓虚拟化技术就是将事物从一种形式转变成另一种形式，最常用的虚拟化技术有操作系统中内存的虚拟化，实际运行时用户需要的内存空间可能远远大于物理机器的内存大小，利用内存的虚拟化技术，用户可以将一部分硬盘虚拟化为内存，而这对用户是透明的。又如，可以利用虚拟专用网技术（VPN）在公共网络中虚拟化一条安全，稳定的“隧道”，用户感觉像是使用私有网络一样。

如果将软PLC安装在虚拟机下，在软PLC出现故障时，用备份的虚拟机代替当前的虚拟机，即可快速恢复系统运行；此外，开发人员不必在现场，即可开发调试项目，在调试完成后，将包含软PLC的虚拟机直接放在现场的工控计算机上就直接可以完全运行。但是软PLC目前只能在物理PC上安装运行，在虚拟机下可以安装，但不能运行，这是由于软PLC需要直接驱动硬件，而虚拟机中的硬件都是虚拟造成的。


## 三、西门子虚拟化WinAC产品分类 

SIMATIC WinAC是西门子公司开发的基于PC控制的核心组件，它的出现扩展了SIMATIC S7的控制范围。WinAC是一个名副其实的控制中心，它将PLC控制、数据处理、通讯、可视化及工艺集成于一台PC机上。 SIMATIC WinAC产品包括软件型和插槽型两大类，包括如下5种产品： 

* 1、WinAC Basis (WinAC 基本型) 
WinAC Basis 是低成本解决方案，用于对控制无精确时间要求，有大量、快速的数据处理与控制任务(控制任务指PLC的控制功能)相结合或其它PC任务的控制场合。
 
* 2、WinAC PN 
第一个支持PROFInet通讯标准的SIMATIC CPU，性能与WinAC Basis相似。WinAC PN支持基于组件的自动化(CBA)和PROFInet通讯标准。基于组件的自动化和PROFInet提供了一个开放的标准，用于在复杂任务中机械和系统单元之间的数据交换。数据交换通过SIMATIC iMap工具来进行配置。WinAC PN适应于以下任务：
整个复杂系统的机械和车间区域之间的协调和连接 来自系统单元或机械可被集成到一个全范围的复杂系统控制WinAC Basis 4.1有一个选件WinAC PN，带有WinAC PN选件的WinAC Basis 4.1支持PROFInet和CBA。
 
* 3、WinAC RTX(WinAC 实时型) 
WinAC RTX 提供了Windows 2000/XP的实时子系统，具有“硬实时”和“抗死机”特性。适应于具有高速和精确时间要求的控制任务的场合，如运动控制、闭环控制等。 

* 4、WinAC MP 
WinAC MP基于WinCE操作系统和SIMATIC MP370(一种多功能面板)硬件平台。MP370为无硬盘、无风扇设计，WinCE具有实时特性，可实现严格的确定性动作。WinAC MP用在恶劣工业环境和有大量数据要处理的场合。 

* 5、WinAC Slot 412/416 
以板卡的形式插入在PC中，在板卡上已经集成了用于控制任务的CPU、存储器等元件。它可独立于PC进行控制操作。板卡上集成一个MPI/DP接口和一个DP口。WinAC Slot适用于对安全性和稳定性要求较高的场合。WinAC Slot 412/416在性能上与S7-412/416相近。


## 四、虚拟控制器WinAC RTX搭建

1、打开虚拟机系统的安装目录，找到后缀名是“.vmx”的文件，然后用记事本打开。

![Alt text](/static/images/WinAC_RTX/1.png)

2、添加虚拟网卡设备，添加如下配置。如果配置文件中已存在，则不添加“ethernet0.virtualDev = "e1000e"”，直接将等号后面的值改为"e1000e"。

    ethernet0.virtualDev = "e1000e"
    bios440.filename="FUJITSU211_314.ROM"
    
![Alt text](/static/images/WinAC_RTX/2.png)

3、在西门子技术支持的官网（[https://support.industry.siemens.com](https://support.industry.siemens.com)）下载文件“FUJITSU211_314.ROM”，并将在虚拟机安装目录下。此文件是将虚拟机硬件映像成FUJITSU PRIMERGR服务器。如下图所示。

![Alt text](/static/images/WinAC_RTX/3.png)

4、打开运行虚拟机，配置当前主机的IP地址。

![Alt text](/static/images/WinAC_RTX/6.png)

5、使用虚拟光驱安装WinAC RTX 2010。

![Alt text](/static/images/WinAC_RTX/4.png)

6、安装完后启动station Configurator。

![Alt text](/static/images/WinAC_RTX/5.png)

7、打开的窗口中添加WinLC RTX，添加通讯网卡“IE 通用”

![Alt text](/static/images/WinAC_RTX/7.png)

8、此时会发现桌面上多出一个图标，此图标就是虚拟PLC的图标，双击打开即可。至此，就完成了在虚拟机中安装PLC。

![Alt text](/static/images/WinAC_RTX/8.png)


## 五、虚拟控制器组态

1、打开step7软件，创建工程，并进行组态配置，配置方法如下图所示。

![Alt text](/static/images/WinAC_RTX/9.png)

2、编写一个小的测试程序。

![Alt text](/static/images/WinAC_RTX/10.png)

3、编译并下载组态程序。

![Alt text](/static/images/WinAC_RTX/11.png)

4、监控运行，如果一切正常，即显示为“RUN”状态。

![Alt text](/static/images/WinAC_RTX/12.png)

5、可以使用step7软件控制虚拟PLC的启停。

![Alt text](/static/images/WinAC_RTX/13.png)

至此，就完成了虚拟PLC的搭建。


