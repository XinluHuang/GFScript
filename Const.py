CONNECT_TYPE_PHONE = 1
CONNECT_TYPE_EMULATOR = 2
CONNECT_TYPE_WIFI = 3
#
# import os, re
#
#
# def judge_legal_ip(one_str):
#     '''
#     正则匹配方法
#     判断一个字符串是否是合法IP地址
#     '''
#     compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
#     if compile_ip.match(one_str):
#         return True
#     else:
#         return False
#
#
# info = os.popen("adb devices").readlines()
# for inx, line in enumerate(info):
#     if inx == 0 or str.strip(line) == "":
#         continue
#     t = str.split(line, '\t')[0]
#     t = str.split(t, ':')[0]
#     print(judge_legal_ip(t))
#     # print(t)
