Title:S7-300/1200TRCV变长度接收
Date: 2018-01-08 14:36
Tags: 工控技术
Authors: feilt


## 1、系统概述
### 1.1 概述
S7-1200 CPU和部分S7-300CPU集成PROFINET通讯接口，支持以太网和基于TCP/IP的通信标准，使用这个通信口可以实现CPU与编程设备、与HMI或触摸屏、以及与其他CPU之间的通信。这个PROFINET是支持10/100Mb/s的RJ45接口，支持电缆交叉自适应，因此标准的或交叉的以太网线都可以使用这个接口。

### 1.2	通信协议
S7-1200/300 CPU的PROFINET通讯接口支持一下通信协议及服务：

* TCP
* ISO on TCP（RCF1006）
* S7通信（服务器端）

### 1.3 物理网络连接
直接连接：CPU直接与CPU、HMI或PLC直接连接通信。也就是说两个通信设备直接连接通信，不需要经过交换机。
![Alt text](/static/images/s7_300_trcv/1.png)

网络连接：多个设备通过交换机相互连接。
![Alt text](/static/images/s7_300_trcv/2.png)

### 1.4 TCP通信流程
![Alt text](/static/images/s7_300_trcv/3.png)

* PLC通过TCON建立连接
* 连接建立后，通过TSEND向目标对象发送数据，通过TRCV接收目标发送的数据。发送和接收可以同时进行。
* 如果断开连接，则不再执行发送命令。也不再执行接收命令。

## 2. TRCV指令参数
### 2.1 TCP不同型号PLC TRCV指令比较
![Alt text](/static/images/s7_300_trcv/4.png)

### 2.2	TRCV管脚参数
![Alt text](/static/images/s7_300_trcv/5.png)

### 2.3 TRCV操作
TRCV 指令将收到的数据写入到通过以下两个变量指定的接收区：

* 指向区域起始位置的指针
* 如果不为 0 则为区域长度或 LEN 上提供的值

说明：
LEN 参数的默认设置 (LEN = 0) 使用 DATA 参数来确定要传送的数据的长度。 确保TSEND 指令传送的 DATA 的大小与 TRCV 指令的 DATA 参数的大小相同。
接收所有作业数据后，TRCV 会立即将其传送到接收区并将 NDR 设置为 1。

### 2.4 TRCV数据输入接收区
![Alt text](/static/images/s7_300_trcv/6.png)
说明：
**特殊模式**
使用 TCP 或 ISO on TCP 协议时可以存在“特殊模式”。 要针对特殊模式组态 TRCV指令，请置位 ADHOC 指令输入参数。 接收区与 DATA构成的区域相同。已接收数据的长度将输出到参数 RCVD_LEN 中。
接收数据块后，TRCV 会立即将数据写入接收区并将 NDR 设置为 1。
如果将数据存储在“优化”DB（仅符号访问）中，则只能接收数据类型为Byte、Char、USInt 和 SInt 的数组中的数据。

## 3. 变长度接收实例
### 3.1 S7-315-2PN/DP
![Alt text](/static/images/s7_300_trcv/7.png)
说明：
在LEN管脚为0的情况下，测得可以变长度接收65528（16382×4）字节。

### 3.2 s7-1212C
![Alt text](/static/images/s7_300_trcv/8.png)

说明：
①图中DATA管脚定义的是接收缓存区的长度，目前测得是8192字节，如果超过8192字节，程序不会报错，但程序不会执行。
②LEN写入65536表示变长度接收。

### 3.3 s7-1215C
![Alt text](/static/images/s7_300_trcv/9.png)
说明：
①图中DATA管脚定义的是接收缓存区的长度，目前测得是65530字节，如果超过65530字节，程序不会报错，但程序不会执行。
②LEN管脚写入接收的数据长度，不能超过8192，超过后程序编译不报错，但不执行。
③ADHOC管脚表示变长度接收，为TRUE有效。如果LEN分配参数（值不超过8192），则接收的长度最大为LEN的长度；如果LEN不分配参数，变长度接收，数值不超过8192字节。

## 4. 总结
这儿只列出了TRCV在3款不同PLC下的不同，实际应用过程PLC型号相似的可以参考上面的参数设置，比如1212C-CD/CD/DC和1212C-DC/DC/Rly，包括不同版本的PLC。由于目前只测试了上面的3款，其他型号PLC可能和上面的不同，比如1214C，s7-1500系列（没有测试）。由于手中没有其他型号的PLC，所以没有测试，如果以后有机会再测。


***参考资料：《SIMATIC S7 S7-1200 可编程控制器系统手册》***
***使用软件：TIA Portal Step7 Professional V14***
***使用硬件：s7-315-2PN/DP v3.2，s7-1212C v3.0，s7-1215C v4.1。***
