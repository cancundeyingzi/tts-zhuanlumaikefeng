def 内容输入函数():
    global 音色, 置顶, 语速, 音调, 风格选项, 风格选择, 内容, 菜单, 主板, cloud, 替换,内容字符提取

    print('输入--直接回车就复述上一句,当前风格', 风格选择)
    输入内容 = input()
    if (输入内容 != ''):  # 判断是否复述,幅度则执行转换
        try:
            # 内容=输入内容.replace(' ', '')#删除所有空格,字符串替换字符
            内容 = ''
            for 内容字符提取 in range(len(输入内容) - 1):
                if 内容字符提取 < len(输入内容) - 1 and 输入内容[内容字符提取] == 'h' and (
                        输入内容[内容字符提取 + 1] == 'h' or 输入内容[内容字符提取 - 1] == 'h'):
                    内容 += '哈'
                else:
                    内容 += 输入内容[内容字符提取]
            else:
                try:#防止输入单个字符的时候报错
                    if 输入内容[内容字符提取 - 1] == 'h':
                        内容 += '哈'
                    else:
                        内容 += 输入内容[内容字符提取 + 1]
                except:
                    pass
            内容 = re.compile(r'([\u4e00-\u9fa5])\s+([\u4e00-\u9fa5])').sub(r'\1\2',
                                                                          内容)  # 参考链接https://blog.csdn.net/u014612521/article/details/100132422
            内容 = re.compile(r'([\u4e00-\u9fa5])\s+([\u4e00-\u9fa5])').sub(r'\1\2',
                                                                          内容)  # \u4e00-\u9fa5是中文,\s是空格,并且要2行,一行不干净
            for key, value in 替换.items():
                内容 = 内容.replace(key, value)
        except:
            print('\033[41m', traceback.format_exc(), '字符替换失败\033[0m')
            return
        if 菜单 in 内容:  # 判断进入菜单
            d = {菜单 + '风格': '风格选择函数()', 菜单 + '文件': '文件函数()',
                 菜单: 'print("""\033[35m当前菜单\n"""+菜单+"""风格,"""+菜单+"""文件\033[0m""")'}  # 启用多行引号防止代码升天,不被识别引号
            eval(d.get(内容,
                       'print("\033[41m触发了菜单,但是没有对应的菜单选项,可以看看有没有输入错误,或者修改热键防止误触\033[0m")'))  # exec没有返回值eval必须有返回值,
            return
        else:
            微软合成函数()
    else:
        播放函数()
