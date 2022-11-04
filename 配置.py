def 读取配置函数函数():
    try:
        dom = xml.dom.minidom.parse('peizhi.xml')
        global 音色, 置顶, 语速, 音调, 风格选项, 风格选择, 内容, 菜单, 主板, cloud, 替换,内容字符提取
        # 0表示配置文件中第一个弹幕前景,1就是表示第二个
        音色 = dom.getElementsByTagName('音色')[0].firstChild.data
        置顶 = dom.getElementsByTagName('置顶')[0].firstChild.data
        语速 = dom.getElementsByTagName('语速')[0].firstChild.data
        音调 = dom.getElementsByTagName('音调')[0].firstChild.data
        菜单 = dom.getElementsByTagName('菜单热键')[0].firstChild.data
        替换 = eval(dom.getElementsByTagName('替换')[0].firstChild.data)  # 上面都是字符串,这个是字典
    except:
        print('\033[41m', traceback.format_exc(), '配置文件呢?是不是改了啥不该改的.去github看看吧缺了啥\033[0m')  # 同时输出报错信息
        input()
    try:  # 后面是联网内容
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.3440.106 Safari/537.36"}
        html = requests.get('https://gitee.com/cancundeyingzi/tts-zhuanlumaikefeng/raw/main/%E7%89%88%E6%9C%AC',
                            proxies={"http": None, "https": None}, headers=headers)
        cloud = eval(str(html.text))  # exec没有返回值eval必须有返回值
        try:
            风格选项 = cloud[音色]
        except:
            风格选项 = "是奇怪的音色!联系我添加一下吧(你要是自己知道支持啥风格,也可以输入,,我这只是方便复制罢了)"
        风格选择 = 'general'
        if cloud['version'] != version:
            os.system("title 有新版本发布,前往github看看有没有新版本吧!")
            print('\033[42m云端版本', cloud['version'], '\033[0m\n\033[42m本地版本', version, '\033[0m')
        else:
            os.system(title)
        print('\033[45m', cloud.get('公告'), '\033[0m')

    except:
        print('\033[41m', traceback.format_exc(), '检测更新失败\033[0m')
        os.system('title 检测更新失败当前版本%s' % (version))
