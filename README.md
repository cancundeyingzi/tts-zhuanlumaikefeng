# tts转录到麦克风
创作初衷:解决电脑语音聊天时没有麦克风/周围嘈杂不方便开麦,与人交流困难的问题     
特点: 
 自动去除空格   
 支持置顶    
 不限制字数   
 自定义说话风格   
 支持没听清复述一次   
 缺点: 微软境外服务器,可能网络不稳定,,但是要稳定只能付钱了,,,好贵的..$16/1M 字符-50w   

需要声音转发软件,下面的这个链接可以下载.
https://github.com/cancundeyingzi/tts-zhuanlumaikefeng/releases/tag/99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
### 简单使用教程
视频教程:https://www.bilibili.com/video/BV11e411K7MY/

首次使用:

1: 把main.exe,peizhi.xml放一起(不建议放桌面,创建个快捷方式就行了)

2: 打开main.exe,寻找虚拟扬声器,并记住前面的代码(如果有好几个一样的随便记一个就行),比如下图

(分辨麦克风扬声器的窍门:'maxInputChannels': 0说明是扬声器.....'maxOutputChannels': 0是麦克风....)

![image](https://user-images.githubusercontent.com/73635883/192142590-80a94a28-f07a-4313-9c4c-32f3975ffafa.png)

3: 关闭软件,用记事本打开peizhi.xml

4: 将<虚拟扬声器设备id>6</虚拟扬声器设备id>中间的数字改成第二步中你记住的代码

(像上图中我把6改成7即可)

5: 再次打开main.exe,输入你要转录的内容即可,记得打开你的录音机并使用虚拟麦克风进行录音!


###  后续使用仅需执行第五步,除非你新建/删除了声卡
