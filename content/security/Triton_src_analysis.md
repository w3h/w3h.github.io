Title:Triton核心源代码分析
Date: 2018-01-08 14:36
Tags: ICS,Triton,恶意软件,施耐德
Authors: w3h


## 事件概述

FireEye麦迪安调查部门的安全研究人员发现一款针对工控系统（ICS）的恶意软件——“TRITON”，该软件瞄准施耐德电气公司Triconex安全仪表控制系统（Safety Instrumented System，SIS）控制器，造成中东一家能源工厂停运。此次攻击事件导致TRITON恶意软件浮出水面。TRITON旨在破坏关键基础设施中广泛使用的 Triconex 安全控制器，通过扫描和映射工业控制系统环境，以便直接向 Triconex安全控制器提供侦察和发布命令。相关专家推测，鉴于经济动机和攻击的复杂程度，可能有国家资助的相关群体参与其中。
下面我们对TRITON恶意软件核心的几个模块的源代码的分析。Trilog.exe是恶意软件的主程序，TsLow.py、TsHi.py、TsBase.py是提供控制器核心通信功能。 

## Trilog.exe分析
经过分析trilog.exe文件是使用py2exe打包的python程序，可以使用[unpy2exe](https://github.com/matiasb/unpy2exe)工具进行反编译。解出的的文件是pyc格式的script_test.py.pyc，再通过[unpyc工具](http://icsmaster.org/download/pyc_uncompile/)将pyc还原成py的源代码。
![Alt text](/static/images/triton/1.png)

![Alt text](/static/images/triton/2.png)

最终解出来的源代码如下图所示：
![Alt text](/static/images/triton/3.png)

![Alt text](/static/images/triton/4.png)

![Alt text](/static/images/triton/5.png)

程序逻辑流程如下：

1. 首先初始化一个TsHi实例对象。
2. 连接输入目标设备（设备IP由参数进行传入），也就是说此文件启动时会传入一个目标设备的IP地址。
3. 连接失败，直接退出程序。
4. 读取文件inject.bin和imain.bin进行拼接，组成最终要下载的数据，如果文件读取失败直接退出程序 。
5. 先下载一段代码，测试增量下载是否成功（PresetStatusField），如果不成功直接返回。
6. 确保下载正常后，将目标的程序进行增量下载（test.SafeAppendProgramMod(data)）
7. 然后循环判断控制器的状态，确定增量下载的程序是否运行正常。
8. 下载失败就强制移除程序。

**流程图如下：**
![Alt text](/static/images/triton/6.png)

## TsLow.py源码分析
此文件是通信最底层的文件，提供基础的UDP的通信，如下图所示。其中udp_ 开头的函数是基础UDP通信函数，tcm_ 和tc_ 开头的函数是对Triconex安全仪表控制系统控制器的报文格式进行封装的通信函数，tcm_ 负责最外一层数据封装，tc_ 负责 tcm_ 结构中的数据字段的封装。
![Alt text](/static/images/triton/7.png)

其中设备探测函数“detect_ip”非常关键，意图非常明显，指定了通信端口为1502，通过UDP协议发送一个特制的广播的报文，接收返回的信息，来判断是否为目标设备，一旦发现目标设备通过端口1502返回信息，则保存设备的IP地址，同时发送一个关闭通信链接的报文给目标设备。此代码明确的告诉我们针对Triconex安全仪表控制系统控制器的探测方法。

![Alt text](/static/images/triton/8.png)

再看tcm_exec函数，通过此函数我们可以分析出控制器的tcm通信报文结构，代码如下图

![Alt text](/static/images/triton/9.png)
![Alt text](/static/images/triton/10.png)

Triconex安全仪表控制系统控制器的TCM通信格式由两个字节的功能码、两个字节的数据字段长度、若干个字节的数据字段、两个字节的CRC校验码组成，典型的TLV格式的通信协议，具体格式如下图所示。
![Alt text](/static/images/triton/e1.png)

再看ts_exec函数，通过此函数我们可以分析出控制器的tc通信报文结构，源代码如下图所示：
![Alt text](/static/images/triton/11.png)

Triconex安全仪表控制系统控制器的TC通信格式由两个字节的未知字段、一个字节的功能码、一个字节的通信计数、两个字节的未知字段、两个字节的校验和
两个字节的长度字段（等于数据字段长度+10）、若干个数据字段组成，格式如下图所示：
![Alt text](/static/images/triton/e2.png)

## TsBase.py源码分析
TsBase类从TsLow继承，主要对控制器的相关功能进行封装，提供上载程序、下载程序，获取版本号，停止程序和运行程序等功能。源代码格式基本都一样，构造对应该功能码的数据包，通过ts_exec函数进行执行。
![Alt text](/static/images/triton/12.png)

控制器相关的功能码，此功能码属于TC层的功能码，如下图所示。
![Alt text](/static/images/triton/e3.png)

## TsHi.py源码分析
此文件是控制器对外的功能接口，所有的函数提供对外的调用，相关函数由程序主函数进行调用，详见trilog.exe分析。下面分析以个常用的函数。

### SafeAppendProgramMod函数分析：
首先获取控制器当前的状态信息，如果运行状态异常（值3）则停止PLC，如果加载状态异常（值5）则取消下载，其它状态直接返回。然后通过上载程序获取工程的Table信息。如下图所示：
![Alt text](/static/images/triton/13.png)
 
“CountFunction”函数通过上载函数获取当前控制器的Function信息。” AppendProgramMin”函数，通过获取的工程信息和Function信息，计算需要申请的空间，然后启动增量下载，将新的工程代码写入控制器。一旦写入失败，则下发取消下载。然后等待获取状态，如果下载成功，直接返回。程序异常时先停止控制器（HaltProgram），接着下载一个基本代码覆盖下载的程序，然后启动控制器（RunProgram）
![Alt text](/static/images/triton/14.png)

![Alt text](/static/images/triton/15.png)
 
### GetCpStatus函数分析：
此函数属于TsBase的函数，使用的功能码是19，返回控制器状态数据包，如下图所示：
![Alt text](/static/images/triton/16.png)
 
## 总结
攻击者对控制器的通信协议非常了解，核心的功能如设备探测、控制器启停等，特别是对程序增量下载的流程非常熟悉，通过增量下载修改控制器的逻辑，一旦成功，隐蔽性非常高，而且目前的安全防御体系根本无法发现，非正常的取证溯源的手段根本无效。但幸庆的是，此攻击过程中一些SIS控制器进入失效的安全状态，自动关闭工业控制流程，导致事件的暴露，TRITION攻击框架从而浮出水面。这是一次典型的针对控制器进行有效攻击的案例，我们也研究过相关的利用手段，一旦恶意攻击者可以控制控制器的程序下载，可以实现很多的功能，比如控制器蠕虫、控制器代理、控制器逻辑炸弹等，攻击的危害是相当大，同时也意味着未来针对控制器的攻击会越来越成熟，我们应该尽快做好相应的安全防范措施，不然攻击来临时我们就会触手无措。





