def 获取音频设备列表函数():
    global 虚拟扬声器设备id
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        声卡 = p.get_device_info_by_index(i)
        if str({k: v for k, v in 声卡.items() if
                v == 'CABLE Input (VB-Audio Virtual C'}) == "{'name': 'CABLE Input (VB-Audio Virtual C'}":
            虚拟扬声器设备id = 声卡.get('index')
            print(声卡)
            break
