Title: 基于WinCC多协议通信实验环境搭建
Date: 2017-05-31 14:36
Tags: 工控技术
Authors: feilt


##一、	概述
目前，随着自动化水平的提高和全厂自动化控制集成的要求，以及基于工业4.0和智能制造的工厂升级和新建工厂的需求。原来单点控制已经不能满足当前的要求。未来方便集成而采用同一家生产商的产品也不太可能。所以现场设备往往有很多设备厂商提供，也造成了不同设备之间通讯、设备和监控平台之间不能直接通讯，单独实现某些设备直接通讯往往也容易增加成本和现场故障点。
当前，随着工业生产的不断发展，工业控制软件取得了长足的进步。然而，由于生产规模的扩大和过程复杂程度的提高，工业控制软件设计面临着巨大的挑战，那就是要集成数量和种类不断增多的现场信息。在传统的控制系统中，智能设备之间及智能设备与控制系统软件之间的信息共享是通过驱动程序来实现的，不同厂家的设备又使用不同的驱动程序，迫使工业控制软件中包含了越来越多的底层通信模块。
当前，比较好的解决方案是使用OPC（OLE for Process Control）来实现不同设备和监控平台的通讯，然后实现设备之间的通讯。为此，本文将讲述一种基于WinCC 7.0和IGS（Industry Gateway OPC Server）的解决方案。

##二、	OPC
OPC是Object Linking and Embedding（OLE）for Process Control的缩写，它是微软公司的对象链接和嵌入技术在过程控制方面的应用。OPC以OLE/COM/DCOM技术为基础，采用客户/服务器模式，为工业自动化软件面向对象的开发提供了统一的标准，

这个标准定义了应用Microsoft操作系统在基于PC的客户机之间交换自动化实时数据的方法。采用这项标准后，硬件开发商将取代软件开发商为自己的硬件产品开发统一的OPC接口程序，而软件开发者可免除开发驱动程序的工作，充分发挥自己的特长，把更多的精力投入到其核心产品的开发上。这样不但可避免开发的重复性，也提高了系统的开放性和可互操作性。

##三、	WinCC
西门子视窗控制中心SIMATIC WinCC（Windows Control Center）是HMI／SCADA软件中的后起之秀，1996年进入世界工控组态软件市场，当年就被美国Control Engnieering杂志评为最佳HMI软件，以最短的时间发展成第三个在世界范围内成功的SCADA系统；而在欧洲，它无可争议地成为第一。 
在设计思想上，SIMATIC WinCC秉承西门子公司博大精深的企业文化理念，性能最全 面、技术最先进、系统最开放的HMI/SCADA软件是WinCC开发者的追求。Wincc是按世 界范围内使用的系统进行设计的，因此从一开始就适合于世界上各主要制造商生产的控制系 统，如A-B，Modicon，GE等，并且通讯驱动程序的种类还在不断地增加。通过OPC的方 式，WinCC还可以与更多的第三方控制器进行通讯。

##四、	结构介绍
WinCC7.0本身已提供A-B PLC的驱动，Modicon的驱动和s7的驱动等，为了更好理解WinCC自带驱动，我们使用SIMATIC S7 PROTOCOL SUITE.chn和s7-300的PLC通讯；为了更好理解OPC，我们不使用Allen Bradley - Ethernet IP.chn和Modbus TCPIP.chn驱动，而是使用OPC.chn。由于A-B PLC和Modbus（本使用Schneider Qunantum PLC）和OPC需要协议转换，自己编写比较麻烦，并且后期维护上级也是不小的工作量，所以，在此我们还需要第三方的OPC server实现不同协议的转换。
以下是系统的结构图。

![Alt text](/static/images/wincc/1.gif)

####4.1 s7协议，建立与s7-300的PLC通讯。
（1）通过step7将wincc和PLC集成到一起（本文为了方便，用户也可也采用分立的方式）。

![Alt text](/static/images/wincc/2.png)

![Alt text](/static/images/wincc/3.png)

![Alt text](/static/images/wincc/4.png)

（2）将WinCC集成到Step7后编译，即为下图，需要的点自动导入到了WinCC中。

![Alt text](/static/images/wincc/5.png)


####4.2 OPC协议，建立1769 PLC 、qunantum PLC和WinCC直接的通讯。
（1）qunantum PLC的数据点。

![Alt text](/static/images/wincc/6.png)

（2）A-B PLC数据点。

![Alt text](/static/images/wincc/7.png)

（3）IGS 建立PLC的数据点

![Alt text](/static/images/wincc/8.png)

####4.3 WinCC建立数据点

![Alt text](/static/images/wincc/9.png)

![Alt text](/static/images/wincc/10.png)

####4.4 WinCC建立画面和连点

![Alt text](/static/images/wincc/11.png)

##五、	运行画面
最终运行的界面如下图所示，实现了三种协议在一个实验环境中运行。

![Alt text](/static/images/wincc/12.jpg)


