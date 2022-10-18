# tts转录到麦克风
注意:gitee版本已发现各种bug,遇到任何问题以github上发布的为准.gitee目前只是自动复制github          
下一步计划:$$$在中文状态输入不便，考虑更换。增加常用语音功能，反复输入同一句常用的话，太傻逼了。输入文件自动识别TXT还是音频。合并检测更新和读取配置函数，精简配置文件，将其转入云服务器存放(已完成)      
长期计划:简易gui，翻译，伪声(角色扮演)支持。       
                 
[配套软件下载](#配套软件下载)   
[简单使用教程](#简单使用教程)      
[进阶朗读设置](#进阶朗读设置)     
[出错解决方法](#出错解决方法)          
  
创作初衷:解决电脑语音聊天时没有麦克风/周围嘈杂不方便开麦,与人交流困难的问题    
亦可用于外语朗读，与外国朋友交流或直接当成普通在线tts使用      
![IMG_0854](https://user-images.githubusercontent.com/73635883/192942723-fb40c5c1-11eb-4088-967e-7e06efdd3311.PNG)

特点:     
 自动去除不小心输入的空格   
 支持置顶    
 不限制字数   
 自定义说话风格语速等   
 支持没听清复述一次   
 支持播放本地音频(虽然有点蠢)     
 缺点: 微软境外服务器,可能网络不稳定,,但是要稳定只能付钱了,,,好贵的..$16/1M 字符-50w   
### 配套软件下载
https://github.com/cancundeyingzi/tts-zhuanlumaikefeng/releases/tag/99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
注意:22.9.29后的版本除了音频驱动，其余全部自带，这个版本以后如果还闪退的话，请直接跳转到[如果还闪退](#如果还闪退)
### 简单使用教程
视频教程:https://www.bilibili.com/video/BV1pt4y1c73o/     
主要功能:         
1: 解压,打开main.exe或者tts.exe          
2: 输入你要转录的内容即可,记得打开你的录音机并调用虚拟麦克风进行录音!              
附加功能:              
1: 播放本地音频:支持标准mp3.flac,ogg.删除软件目录下的一切音频文件,把你要放的音频复制到软件目录下,重命名成1.在软件显示输入--直接回车就复述上一句时回车          
2: 修改语气,朗读文本文档(txt):在软件显示输入--直接回车就复述上一句时输入$$$风格选择,或者$$$文件,,如果忘记了,可以输入$$$查看当前支持的$$$即时菜单        
### 进阶朗读设置:    
自己看peizhi.xml,         
https://azure.microsoft.com/zh-cn/products/cognitive-services/text-to-speech/#features   中文体验测试            
https://learn.microsoft.com/zh-cn/azure/cognitive-services/speech-service/language-support?tabs=stt-tts           外语朗读人列表           
# 出错解决方法(22.10及以后版本压缩包已内置)
没配置ffmpeg的环境变量,你可以自己去下载,也可以去上面配套软件下载那边下载ffmpeg.7z压缩包.         
直接解压到main.exe的目录,最终应该如图所示(后面还有一些截图截不下了)           
![image](https://user-images.githubusercontent.com/73635883/192148038-38455b28-baea-45bb-bb2d-89ab06c5624e.png)
## 如果还闪退         
如图输入cmd,回车                    
![image](https://user-images.githubusercontent.com/73635883/192148068-5faf5101-37a1-43e2-aafa-283c58979b99.png)             
输入main.exe,回车    
![image](https://user-images.githubusercontent.com/73635883/192148110-7dfaf260-e518-4fe3-bb46-d7124564e6f7.png)               
然后怎么闪退你操作一遍,这次就会输出报错信息不闪退了...你把报错的内容发我看看,我修复一下.            
## ~~win7等提示无法启动此程序丢失api-ms-win-core(从22.10开始压缩包内置,已经无需下载)
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
regsvr32 c:\windows\syswow64\"filename".dll~~           
![image](https://user-images.githubusercontent.com/73635883/194858246-108fe7f6-4950-49eb-a49f-0d7c398ff73d.png)                      
风格参考,具体应该不会那么复杂,ctrl+回车发送            
输入框为空时点播放就是复制上一句/播放自定义音乐.     
文件输入自动判断纯文本/音频.      
所以不区分大块,翻译也和文本做一起算了,问题应该不是很大,但愿空间够用(长文本不推荐使用这个翻译)
