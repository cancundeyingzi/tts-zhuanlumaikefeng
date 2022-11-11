def 文件函数():
    global 音色, 置顶, 语速, 音调, 风格选项, 风格选择, 内容, 菜单, 主板, cloud, 替换,内容字符提取
    root = tk.Tk()
    root.withdraw()
    文件地址 = filedialog.askopenfilename()  # 斜杠方向目前好像没关系,,,具体不知道/,\(\\),\\(\\\\)好像都能跑.........
    文件后缀 = 文件地址.split(".")[-1].lower()  # 将字符串按.分段,0第一段,1第二段,-1倒数第一段(分段后会删除.)字符串分段,分割,并且改成小写,防止不认识MP3,FLAC等大写
    备选音乐后缀 = ["mp3", "flac", "ogg"]
    if 文件后缀 in 备选音乐后缀:
        # if (os.path.exists('./1.mp3')):#现在已经不需要
        #     # 存在，则删除文件
        #     os.remove('./1.mp3').........
        shutil.copyfile(文件地址, './1.' + 文件后缀)  # 重命名+移动
        内容 = 文件地址
        转换函数(文件后缀)
    else:
        try:
            with open(文件地址, "r", encoding='gb18030') as f:  # 打开文件
                内容 = f.read()  # 读取文件
        except:
            try:
                with open(文件地址, "r", encoding='utf-8') as f:  # 打开文件
                    内容 = f.read()  # 读取文件
            except:
                print('\033[41m文件错误,不是MP3/flac/ogg后缀,也无法用gb18030(GBK)或utf-8作为文本打开.\033[0m')
                return
        微软合成函数()
