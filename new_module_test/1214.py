# -*- coding: utf-8 -*-
# @Time    : 2018/12/14 12:58
import getopt
import sys
# print(sys.argv)
# opts, args = getopt.getopt(sys.argv[1:], "hi:o:", ["help", "c=", 'a='])
# print (opts,args)

# try:
#     options,args = getopt.getopt(sys.argv[1:],"hp:i:",["help","ip=","port="])
#     print('options{}args{}'.format(options,args))
# except getopt.GetoptError:
#     sys.exit()
#
# for name,value in options:
#     if name in ["-h","--help"]:
#         print('a')
#     if name in ["-i","--ip"]:
#         print ('ip is----',value)
#     if name in ["-p","--port"]:
#         print ('port is----',value)
#
#
#
# try:
#     options, args = getopt.getopt(sys.argv[1:], "hp:i:", ["help", "ip=", "port="])
#     print('options{}args{}'.format(options, args))
# except getopt.GetoptError:
#     sys.exit()
#
# for name, value in options:
#     if name in ["-h", "--help"]:
#         print('a')
#     if name in ["-i", "--ip"]:
#         print ('ip is----', value)
#     if name in ["-p", "--port"]:
#         print ('port is----', value)

# import socket
#
#
# def get_host_ip():
#     try:
#         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         s.connect(('114.114.114.114', 80))
#         ip = s.getsockname()[0]
#     finally:
#         s.close()
#
#     return ip
#
#
# print(get_host_ip())



# try:
#     a=10/0
# except:
#     print('aaaaa')
#     sys.exit(2)



# import sys,os,subprocess
# from subprocess import Popen,PIPE
# p2 = Popen('cd',shell=True,stdout=PIPE,cwd='/home/myself/new_module_test')
# p2.wait()
# print ("当前目录:%s" %p2.stdout.read())

# import rsa
# # 生成密钥
# (pubkey, privkey) = rsa.newkeys(2048)
#
# #
# print(pubkey.save_pkcs1().decode())
# print(privkey.save_pkcs1().decode())
#
# # 保存密钥
# with open('public.pem', 'w+') as f:
#     f.write(pubkey.save_pkcs1().decode())
#
# with open('private.pem', 'w+') as f:
#     f.write(privkey.save_pkcs1().decode())

# # 导入密钥
# with open('public.pem', 'r') as f:
#     pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
#
# with open('private.pem', 'r') as f:
#     privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
# #
# # 明文
# message = 'hello'

# # 公钥加密
# crypto = rsa.encrypt(message.encode(), pubkey)
# print(crypto)
#
# # 私钥解密
# message = rsa.decrypt(crypto, privkey).decode()
# print(message)
# #
# 私钥签名
# signature = rsa.sign(message.encode(), privkey, 'SHA-1')
# # print(signature)
#
# # 公钥验证
# result=rsa.verify(message.encode(), signature, pubkey)
# print(result)

# import sys
# print('目前系统的编码为：',sys.getdefaultencoding())
# name='小明'
# print(type(name)) # 首先我们来打印下转码前的name类型，因为它是str，所以可以通过encode来进行编码
# name1=name.encode('utf-8')
# print(name1)
#
#
# name2=name1.decode('utf-8')
# print(type(name2))
# print(name2)
#
# name3=name2.encode('gbk')
# name4=name3.decode('gbk')
# print(type(name3))
# print(name3)
# print(name4)


# def a():
#     print('aaa')
# print('bbb')
#
# if __name__=='__main__':
#     a()


import configparser
config = configparser.ConfigParser()
config.readfp(open('setting.ini'))
a = config.get("ZIP","MD5")
print (a)
















