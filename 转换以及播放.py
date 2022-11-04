def 转换函数(文件后缀):
    try:
        if 文件后缀 == 'mp3':
            dst = "1.wav"
            audSeg = AudioSegment.from_mp3("1.mp3")
            audSeg.export(dst, format="wav")
        elif 文件后缀 == 'flac':
            dst = "1.wav"
            audSeg = AudioSegment.from_file("1.flac")
            audSeg.export(dst, format="wav")
        else:
            dst = "1.wav"
            audSeg = AudioSegment.from_ogg("1.ogg")
            audSeg.export(dst, format="wav")

    except:
        print('\033[41m', traceback.format_exc(),
              'mp3/flac/ogg转换到wav失败了,你看看有没有ffmpeg一类的东西,没有的话去我github下载ffmpeg.7z并且解压过来吧\033[0m')
        return
    print('文件转换完成')
    播放函数()


def 播放函数():
    try:
        print("开始播放")
        CHUNK = 1024
        # 从目录中读取语音
        wf = wave.open('1.wav', 'rb')
        # read data
        data = wf.readframes(CHUNK)
        # 创建播放器
        p = pyaudio.PyAudio()
        # 获得语音文件的各个参数
        FORMAT = p.get_format_from_width(wf.getsampwidth())
        if FORMAT == 1:
            FORMAT = 2
            print('\033[31;44m', FORMAT, '遇到bug,已经尝试修复.若音频播放不正确请及时反馈,并且关闭程序!!!!!!\033[0m')
            time.sleep(1)
        CHANNELS = wf.getnchannels()
        RATE = wf.getframerate()
        # 打开音频流， output=True表示音频输出
        stream = p.open(format=FORMAT,
                        output_device_index=int(虚拟扬声器设备id),  # 虚拟扬声器设备id,#接上上面的设备选择7
                        channels=CHANNELS,
                        rate=RATE,
                        frames_per_buffer=CHUNK,
                        output=True)
        # play stream (3) 按照1024的块读取音频数据到音频流，并播放
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)
            print(内容)
        print("播放完成")
    except:
        print('\033[41m', traceback.format_exc(), '找不到1.wav,你不会啥都没输入就在复述上一句吧......\033[0m')
        return
