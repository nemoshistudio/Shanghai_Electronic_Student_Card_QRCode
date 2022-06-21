# coding:utf-8
#By 西位nemo
#电子学生证二维码生成py版

import webbrowser
import qrcode

print('--------------------------------------------')
print()
print('上海市电子学生证二维码生成器')
print()
print('By 西位Nemo施')
print()
print('声明：本程序通过并结合 自有 电子学生证 逆向推理进行开发、测试')
print()
print('--------------------------------------------')

#获取个人信息
print('请正确填写自己的个人信息')
print('如信息错误将导致二维码无法正常使用')
print()
print('--------------------------------------------')
print()
name = input('1.姓名： ')
sex = input('2.性别（男/女）： ')
studentid = input('3.学生证号： ')
personalid = input('4.身份证号： ')

#确认信息
print('--------------------------------------------')
print('请确认各项个人信息')
print()
print('1.姓名：    ' + name)
print('2.性别：    ' + sex)
print('3.学生证号： ' + studentid)
print('4.身份证号： ' + personalid)
print('--------------------------------------------')

verify = input('如有错误，请输入错误项编号；如无错误，请输入 y ： ')
print('--------------------------------------------')

while not verify == 'y':

    if verify == '1':
        name = input('姓名：')

    if verify == '2':
        sex = input('性别（男/女）：')

    if verify == '3':
        studentid = input('学生证号：')

    if verify == '4':
        personalid = input('身份证号：')


    print('请再次确认各项个人信息')
    print('1.姓名：   ' + name)
    print('2.性别：   ' + sex)
    print('3.学生证号：' + studentid)
    print('4.身份证号：' + personalid)
    print()

    verify = input('如有错误，请输入错误项编号；如无错误，请输入 y ： ')
    print('--------------------------------------------')

#编码信息/字符串转字节
namecache = name #文件名身份备份
slash = bytes('/',encoding='utf8')
name = bytes(name,encoding='utf8')
sex = bytes(sex,encoding='utf8')
studentid = bytes(studentid,encoding='utf8')
personalid = bytes(personalid,encoding='utf8')

#合并信息
sum = name + slash + sex + slash + studentid + slash + personalid

#加入UTF-8 头部 BOM
num = b'\xef\xbb\xbf' + sum

#生成二维码
#设置二维码规格
qr = qrcode.QRCode(version = 4,
                   error_correction = qrcode.constants.ERROR_CORRECT_M,
                   )

#生成二维码
qr.add_data(num)
img = qr.make_image()
namecache = namecache +' 的 电子学生证二维码.jpg'
img.save(namecache)

print()
print('二维码已保存至当前目录下')
print()
print('文件名为：' + namecache)
print()
print('--------------------------------------------')
print('输入 e 退出 ；'
      '输入 v 访问 Github 源代码仓库')
exit = input()
if exit == 'v':
    webbrowser.open('https://github.com/nemoshistudio/Shanghai_Electronic_Student_Card_QRCode')

