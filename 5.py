from tkinter import *

root = Tk()
root.title("물건 챙김 알리미")
root.geometry("600x900")
root.resizable(False, False)


Label_stuff= Label(root, text = "물건챙김 알리미",
               font = ("Consolas", 40))
Label_stuff.place(relx=0.5, rely= 0.15, anchor='center')

Mode_setting = 1
Mode = Label(root, text = "MODE = 기본설정",
               font = ("Consolas", 30))
Mode.place(relx=0.5, rely= 0.9, anchor='center')

def destroy():
    Label_stuff.destroy()
    Mode.destroy()
    Basic_setting.destroy()
    Study_settings.destroy()
    PC_room_setting.destroy()
    SCAN.destroy()

def Mode_Basic_setting():
    Mode.config(text="MODE = 기본설정")
    Mode_setting = 1

def Mode_Study_settings():
    Mode.config(text="MODE = 공부용 설정")
    Mode_setting = 2

def Mode_PC_room_setting():
    Mode.config(text="MODE = PC방용 설정")
    Mode_setting = 3

global Basic_setting
Basic_setting = Button(root, text = "기본 설정",
               font = ("한컴 고딕", 20), command= Mode_Basic_setting)
Basic_setting.place(relx=0.5, rely= 0.3, anchor='center')

global Study_settings
Study_settings = Button(root, text = "공부용 설정",
               font = ("한컴 고딕", 20), command= Mode_Study_settings)
Study_settings.place(relx=0.5, rely= 0.4, anchor='center')

global PC_room_setting
PC_room_setting = Button(root, text = "PC방용 설정",
               font = ("한컴 고딕", 20), command= Mode_PC_room_setting)
PC_room_setting.place(relx=0.5, rely= 0.5, anchor='center')

global SCAN
SCAN = Button(root, text = "SCAN",
               font = ("Consolas", 40), command= destroy)
SCAN.place(relx=0.5, rely= 0.7, anchor='center')

