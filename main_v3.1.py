# coding:utf-8
#By 西位nemo
#电子学生证二维码生成py版

import webbrowser
import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pyzbar.pyzbar as pyzbar
import cv2


print('--------------------------------------------')
print()
print('上海市电子学生证二维码生成器 v2')
print()
print('By 西位Nemo施')
print()
print('声明：本程序通过并结合 自有 电子学生证 逆向推理进行开发、测试')
print()
print('--------------------------------------------')

mode = input('请选择生成二维码的方式（1 或 2 或 3）：\n\n'
             '1.自行填入各项个人信息\n\n'
             '2.识别拍摄好的学生证二维码并生成信息（推荐）\n\n'
             '3.打开相机识别学生证二维码并生成信息（不推荐）\n\n')

if mode == '1':

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

if mode == '2':
    print()
    print('请选择拍摄好的清晰的学生证图片')
    root = tk.Tk()
    root.withdraw()

    Filepath = filedialog.askopenfilename(title='请选择照片')  # 获得选择好的文件

    img = Image.open(Filepath)
    barcodes = pyzbar.decode(img)

    for barcode in barcodes:
        barcode_content = barcode.data.decode('utf-8')  # 二维码内容


    print('--------------------------------------------')
    print('姓名：' + barcode_content[0:3])
    print('性别：' + barcode_content[4:5])
    print('学籍号：' + barcode_content[6:25])
    print('身份证号：' + barcode_content[26:44])
    print('--------------------------------------------')
    verify = input('请确认以上信息是否正确,正确请输入 y，错误请输入 n\n')
    print('--------------------------------------------')

    while not verify == 'y':
        print()
        print()
        print('请重新选择拍摄好的清晰的学生证图片')
        root = tk.Tk()
        root.withdraw()

        Filepath = filedialog.askopenfilename(title='请选择照片')  # 获得选择好的文件

        img = Image.open(Filepath)
        barcodes = pyzbar.decode(img)
        print('--------------------------------------------')

        for barcode in barcodes:
            barcode_content = barcode.data.decode('utf-8')  # 二维码内容


        print('--------------------------------------------')
        print('姓名：' + barcode_content[0:3])
        print('性别：' + barcode_content[4:5])
        print('学籍号：' + barcode_content[6:25])
        print('身份证号：' + barcode_content[26:44])
        print('--------------------------------------------')
        verify = input('请再次确认以上信息是否正确,正确请输入 y，错误请输入 n\n')

    sum = bytes(barcode_content,encoding='utf8')
    namecache = barcode_content[0:3]

if mode == '3':
    print('Tips：可以先用手机拍一张照，放大后便于识别')
    def scan_qrcode(qrcode):
        data = pyzbar.decode(qrcode)
        return data[0].data.decode('utf-8')


    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('scan qrcode', frame)

        # 解析二维码
        text = None
        try:
            text = scan_qrcode(frame)
        except Exception as e:
            pass
        if text:
            cv2.destroyAllWindows()

            print('--------------------------------------------')
            print('姓名：' + text[0:3])
            print('性别：' + text[4:5])
            print('学籍号：' + text[6:25])
            print('身份证号：' + text[26:44])
            print('--------------------------------------------')
            verify = input('请确认以上信息是否正确,正确请输入 y，错误请输入 n\n')
            print('--------------------------------------------')

            if verify == 'y':
                break

            print('请重新识别')
            print('Tips：可以先用手机拍一张照，放大后便于识别')

        key = cv2.waitKey(10)
        if key == ord('q'):
            break
    cv2.destroyAllWindows()

    sum = bytes(text, encoding='utf8')
    namecache = text[0:3]

#加入UTF-8 头部 BOM
num = b'\xef\xbb\xbf' + sum


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

