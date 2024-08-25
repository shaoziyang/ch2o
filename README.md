# DIY a simple ch2o detection system (DIY一个简单的CH2O检测系统)

本 DIY 项目是制作一个可以远程访问的 ch2o 检测仪，不但可以查看当前数值，还可以查看历史数据曲线，甚至可以远程查看。只需要很少的元器件，编写少量代码，很快就可以实现一个完整功能的检测系统。项目包括了硬件、服务器、网页等部分，是一个完整的可运行系统。

硬件部分使用了 ESP32 作为控制器，通过 micropython 编程，传感器和接收器之间通过 espnow 通信，可以方便的扩展更多传感器和功能，组成一个小的传感器网络。

项目中使用了树莓派了作为数据服务器和网页服务器，但也可以使用其它类似功能的派，或者普通计算机，甚至可以使用运行 armbian 系统的机顶盒。可以在 Linux 或 Windows 等系统中使用。服务器上只需要安装 python、apache2 和 PHP，无需数据库。

项目提供了一个演示网站，网址是：[https://rpi.kodview.com/ch2o/](https://rpi.kodview.com/ch2o/)。

为了方便在 windows 下的使用，还特别提供一个 windows 的便携精简版服务器（可以放在U盘或移动硬盘中运行），包括了 apache2 和 PHP 以及必要的扩展，以及ch2o项目的额文件，可以直接运行。如果需要修改配置，以及升级服务器软件版本，可以参考软件中的说明。这个精简版服务器还包括了一个基于wikidocs的文档管理和网址导航系统，里面存放了几个DIY项目的资料（包括这个DIY一个多功能甲醛检测仪项目），以后社区的一些资料也会以这种方式共享发布出来。为了减少文件大小，精简版服务器中没有打包kodbox，如果需要使用，可以自行安装一下，必要的服务器扩展已经集成了。


详细的 DIY 步骤和说明，请参阅下面的微信订阅号。


微信订阅号：

* [DIY一个多功能甲醛检测仪（一）](https://mp.weixin.qq.com/s/mmEKNzwPQLi_3NApjSGceQ)
* [DIY一个多功能甲醛检测仪（二）](https://mp.weixin.qq.com/s/PinbINwd2Ei67nEK1hWbbQ)
* [DIY一个多功能甲醛检测仪（三）](https://mp.weixin.qq.com/s/q0dW9oIHGCAA1u4OpM74LQ)

本项目仅作为参考，作者不对内容提供任何形式的担保。

[micropython中文社区](https://www.micropython.org.cn)
