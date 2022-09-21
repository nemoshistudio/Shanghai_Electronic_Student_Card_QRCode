# coding:utf-8
#By 西位nemo
#电子学生证二维码生成py GUI版

from tkinter import *
import tkinter
import webbrowser
import qrcode
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pyzbar.pyzbar as pyzbar
import sys

class GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    def set_init_window(self):
        global name
        global sex
        global studentid
        global personalid
        global Filepath
        global barcode_content

        name = ""
        sex = ""
        studentid = ""
        personalid = ""

        self.init_window_name.title("学生证二维码生成器")
        self.init_window_name.geometry('540x864+100+100')
        self.init_window_name["bg"] = "white"

        self.exit_button = Button(self.init_window_name, bg='gray', relief='sunken',height=1,width=8, text='退出',command=self.exit_all)
        self.exit_button.grid(row=15, column=1)

        self.choose_button = Button(self.init_window_name, bg='gray', relief='sunken',height=1,width=20, text='选择拍摄的二维码照片',command=self.choose)
        self.choose_button.grid(row=11, column=1)

        self.choose_button = Button(self.init_window_name, bg='gray', relief='sunken', height=1, width=8,text='生成', command=self.make)
        self.choose_button.grid(row=7, column=1)

        self.choose_button = Button(self.init_window_name, bg='gray', relief='sunken', height=1, width=8, text='保存',command=self.savefile)
        self.choose_button.grid(row=12, column=1)

        self.init_start_label = Label(self.init_window_name, bg='white', height=2, text="名字:")
        self.init_start_label.grid(row=2, column=0)
        self.init_start_label = Label(self.init_window_name, bg='white', height=2, text="性别:")
        self.init_start_label.grid(row=3, column=0)
        self.init_start_label = Label(self.init_window_name, bg='white', height=2, text="学生证号:")
        self.init_start_label.grid(row=4, column=0)
        self.init_start_label = Label(self.init_window_name, bg='white', height=2, text="身份证号:")
        self.init_start_label.grid(row=5, column=0)
        self.init_start_label = Label(self.init_window_name, bg='white', height=2, text="可以直接输入，也可以选取拍摄的二维码照片")
        self.init_start_label.grid(row=6, column=1)

        self.name_text = Text(self.init_window_name, bg='gainsboro', relief='sunken', width=50, height=1)
        self.name_text.grid(row=2, column=1)
        self.sex_text = Text(self.init_window_name, bg='gainsboro', relief='sunken', width=50, height=1)
        self.sex_text.grid(row=3, column=1)
        self.studentid_text = Text(self.init_window_name, bg='gainsboro', relief='sunken', width=50, height=1)
        self.studentid_text.grid(row=4, column=1)
        self.personalid_text = Text(self.init_window_name, bg='gainsboro', relief='sunken', width=50, height=1)
        self.personalid_text.grid(row=5, column=1)

    def exit_all(self):

        sys.exit(0)

    def visit_github(self):
        webbrowser.open('https://github.com/nemoshistudio/Shanghai_Electronic_Student_Card_QRCode')

    def savefile(self):
        root = tk.Tk()
        root.withdraw()
        Folderpath = filedialog.askdirectory()
        imgtemp = Image.open('C:/Users\Public\Pictures\preview.jpg')
        imgtemp.save(Folderpath + '/' + name + ' 的 电子学生证二维码.jpg')

    def make(self):
        barcode_content = name + "/" + sex + "/" + studentid + "/" + personalid

        sum = bytes(barcode_content, encoding='utf8')
        num = b'\xef\xbb\xbf' + sum
        qr = qrcode.QRCode(version=4,
                           error_correction=qrcode.constants.ERROR_CORRECT_M,
                           )

        # 生成二维码
        qr.add_data(num)
        img = qr.make_image()
        img.save('C:/Users\Public\Pictures\preview.jpg')
        filename = name + ' 的 电子学生证二维码.jpg'
        imgtemp = tkinter.PhotoImage(file='C:/Users\Public\Pictures\preview.jpg')
        self.init_start_label = Label(self.init_window_name, image=imgtemp)
        self.init_start_label.grid(row=9, column=1)
        self.init_start_label = Label(self.init_window_name, bg='white', height=2, text=filename)
        self.init_start_label.grid(row=10, column=1)

    def choose(self):
        global name
        global sex
        global studentid
        global personalid
        global Filepath
        global barcode_content

        root = tk.Tk()
        root.withdraw()

        Filepath = filedialog.askopenfilename(title='请选择照片')

        img = Image.open(Filepath)
        barcodes = pyzbar.decode(img)

        for barcode in barcodes:
            barcode_content = barcode.data.decode('utf-8')

        if barcode_content[2] == '/':
            name = barcode_content[0:2]
            sex = barcode_content[3:4]
            studentid = barcode_content[5:24]
            personalid = barcode_content[25:43]

        if barcode_content[3] == '/':
            name = barcode_content[0:3]
            sex = barcode_content[4:5]
            studentid = barcode_content[6:25]
            personalid = barcode_content[26:44]

        if barcode_content[4] == '/' and not barcode_content[2] == '/':
            name = barcode_content[0:4]
            sex = barcode_content[5:6]
            studentid = barcode_content[7:26]
            personalid = barcode_content[27:45]

        src = self.name_text.get(1.0, END).strip().replace("\n", "").encode()
        self.name_text.delete(1.0, END)
        self.name_text.insert(1.0, name)

        src = self.sex_text.get(1.0, END).strip().replace("\n", "").encode()
        self.sex_text.delete(1.0, END)
        self.sex_text.insert(1.0, sex)

        src = self.studentid_text.get(1.0, END).strip().replace("\n", "").encode()
        self.studentid_text.delete(1.0, END)
        self.studentid_text.insert(1.0, studentid)

        src = self.personalid_text.get(1.0, END).strip().replace("\n", "").encode()
        self.personalid_text.delete(1.0, END)
        self.personalid_text.insert(1.0, personalid)

def gui_start():
    init_window = Tk()  
    Vocabulary_writing = GUI(init_window)
    Vocabulary_writing.set_init_window()
    init_window.mainloop()

gui_start()
