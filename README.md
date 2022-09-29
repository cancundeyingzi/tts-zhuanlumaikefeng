# tts转录到麦克风
创作初衷:解决电脑语音聊天时没有麦克风/周围嘈杂不方便开麦,与人交流困难的问题    
亦可用于外语朗读，与外国朋友交流或直接当成普通在线tts使用      
![IMG_0854](https://user-images.githubusercontent.com/73635883/192942723-fb40c5c1-11eb-4088-967e-7e06efdd3311.PNG)

特点:     
 自动去除不小心输入的空格   
 支持置顶    
 不限制字数   
 自定义说话风格   
 支持没听清复述一次   
 缺点: 微软境外服务器,可能网络不稳定,,但是要稳定只能付钱了,,,好贵的..$16/1M 字符-50w   
### 配套软件下载.
https://github.com/cancundeyingzi/tts-zhuanlumaikefeng/releases/tag/99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
### 简单使用教程
视频教程:https://www.bilibili.com/video/BV11e411K7MY/       
首次使用:         
1: 把main.exe,peizhi.xml放一起(不建议放桌面,创建个快捷方式就行了)      
~~2: 打开main.exe,寻找虚拟扬声器,并记住前面的代码(如果有好几个一样的随便记一个就行),比如下图~~        
~~(分辨麦克风扬声器的窍门:'maxInputChannels': 0说明是扬声器.....'maxOutputChannels': 0是麦克风....)~~         
![image](https://user-images.githubusercontent.com/73635883/192142590-80a94a28-f07a-4313-9c4c-32f3975ffafa.png)            
~~3: 关闭软件,用记事本打开peizhi.xml~~         
~~4: 将<虚拟扬声器设备id>6</虚拟扬声器设备id>中间的数字改成第二步中你记住的代码~~         
~~(像上图中我把6改成7即可)~~          
5: 再次打开main.exe,输入你要转录的内容即可,记得打开你的录音机并调用虚拟麦克风进行录音!              
### 进阶朗读设置:    
https://azure.microsoft.com/zh-cn/products/cognitive-services/text-to-speech/#features   中文体验测试            
https://learn.microsoft.com/zh-cn/azure/cognitive-services/speech-service/language-support?tabs=stt-tts           外语朗读人列表           
# 出错解决方法
~~大概率你没配置ffmpeg的环境变量,你可以自己去下载,也可以去上面配套软件下载那边下载ffmpeg.7z压缩包.~~         
~~直接解压到main.exe的目录,最终应该如图所示(后面还有一些截图截不下了)~~           
![image](https://user-images.githubusercontent.com/73635883/192148038-38455b28-baea-45bb-bb2d-89ab06c5624e.png)
## ~~如果还闪退~~         
~~如图输入cmd,回车~~                    
![image](https://user-images.githubusercontent.com/73635883/192148068-5faf5101-37a1-43e2-aafa-283c58979b99.png)             
~~输入main.exe,回车~~    
![image](https://user-images.githubusercontent.com/73635883/192148110-7dfaf260-e518-4fe3-bb46-d7124564e6f7.png)               
~~然后怎么闪退你操作一遍,这次就会输出报错信息不闪退了...你把报错的内容发我看看,我修复一下.~~            
## win7等提示无法启动此程序丢失api-ms-win-core.........    
还是上面配套软件下载把api-ms-win-core-path-l1-1-0.dll放到你的系统路径。它的默认路径是在：   
C:\Windows\System (Windows 95/98/Me),   
C:\WINNT\System32 (Windows NT/2000),   
C:\Windows\System32 (Windows XP, Vista, 7, 8, 8.1, 10).   
在 64位 Windows 上，32位 DLL 文件的默认路径是C:\Windows\SysWOW64\，    
64 位 DLL 文件在C:\Windows\System32\ 。       
重启电脑。     
如果问题仍未解决，按以下步骤注册 DLL 文件：         
32 位 DLL 文件用在 32 位 Windows 上，64 位 DLL 文件用在 64 位 Windows 上：             
打开一个提升权限运行的命令行窗口。          
具体操作是点击“开始”，点击“所有程序”，点击“附件”，右键点击“命令提示符”，然后点击“以管理员权限运行”。          
在 Windows 8/10 中，前往“开始”界面。键入“cmd”， Windows 会找到“命令行提示符”。右键点击“命令提示符”，选择“以管理员权限运行”。      
如果要求输入管理员密码或确认，输入密码，或点击“允许”。        
输入 regsvr32 “filename".dll 然后按下回车。            
将 32 位 DLL 文件注册到一台 64 位 Windows 上：          
按前述方法打开一个提升权限运行的命令行窗口。          
在命令行中键入：        
cd c:\windows\syswow64\         
然后键入以下命令并回车：           
regsvr32 c:\windows\syswow64\"filename".dll           
