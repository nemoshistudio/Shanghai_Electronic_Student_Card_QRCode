#By 西位nemo
#电子学生证二维码生成py版

import qrcode

print('上海市电子学生证二维码生成器')
print()
print('By 西位Nemo施')
print()
print('--------------------------------------------')

#获取个人信息
print('请正确填写自己的个人信息')
name = input('姓名： ')
sex = input('性别（男/女）： ')
studentid = input('学生证号： ')
personalid = input('身份证号： ')

#确认信息
print('--------------------------------------------')
print('请确认各项个人信息')
print('1.姓名：   ' + name)
print('2.性别：   ' + sex)
print('3.学生证号：' + studentid)
print('4.身份证号：' + personalid)
print('--------------------------------------------')

verify = input('如有错误，请输入错误项编号；如无错误，请输入 y ')

while not verify == 'y':

    if verify == '1':
        name = input('姓名')

    if verify == '2':
        sex = input('性别（男/女）')

    if verify == '3':
        studentid = input('学生证号')

    if verify == '4':
        personalid = input('身份证号')

    print('--------------------------------------------')
    print('请再次确认各项个人信息')
    print('1.姓名：   ' + name)
    print('2.性别：   ' + sex)
    print('3.学生证号：' + studentid)
    print('4.身份证号：' + personalid)
    print()

    verify = input('如有错误，请输入错误项编号；如无错误，请输入 y ')
#合并信息
num = name + '/' + sex +'/' + studentid +'/' + personalid

#生成二维码
#设置二维码规格
qr = qrcode.QRCode(version = 4,
                   error_correction = qrcode.constants.ERROR_CORRECT_M,
                   )

#生成二维码
qr.add_data(num)
img = qr.make_image()
img.save( name +' 的 电子学生证二维码.jpg')
print('--------------------------------------------')
print('二维码已保存至当前目录下')
print()
print('按回车退出')
exit = input()

