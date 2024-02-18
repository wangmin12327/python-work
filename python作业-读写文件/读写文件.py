#以只写入文件的方式打开index.html文件
file = open(r"D:\开发项目\python-work\python作业-读写文件\index.html","w")
#写入数据
file.write("<h1>HelloWorld</h1>")
file.write("\n")
file.write("<p>这是一个html文件</p>\n")
#关闭文件
file.close()

#以只写入二进制字符串内容的方式打开index.html文件
#要将字符串转换成 bytes类型的二进制字符串,函数返回成功写入数据的长度
str = "abcde\n"
bin = str.encode("UTF-8")
file = open(r"D:\开发项目\python-work\python作业-读写文件\index.html","ab")
file.write(bin)
#关闭文件
file.close()

#写入一序列的字符串
file = open(r"D:\开发项目\python-work\python作业-读写文件\index.html","a")
datas = ['a\n','b\n','c\n','d\n']
file.writelines(datas)
#关闭文件
file.close()

# #以只读取文件的方式打开index.html文件
# file = open(r'D:\开发项目\python-work\python作业-读写文件\index.html','r')
# #读取十个字符
# content = file.read(5)
# print(content)
# #关闭文件
# file.close()

#以只读取文件的方式打开index.html文件
file = open(r'D:\开发项目\python-work\python作业-读写文件\index.html','r')
#读取所有内容
content = file.read()
print(content)
#关闭文件
file.close()