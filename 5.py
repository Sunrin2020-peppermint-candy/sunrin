from tkinter import *

from PIL import ImageTk
from PIL import Image

from scan import scan_func

import cv2

HAVE_TO_TAKE = {
    1: ['cell phone']
    2: ['cell phone', 'backpack']
    3: ['cell phone', 'wallet']
}

cap = cv2.VideoCapture(0)

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

    detected.place(relx=0.5, rely= 0.2, anchor='center')
    hasnt_take.place(relx=0.5, rely= 0.9, anchor='center')
    videoCapture()

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
Basic_setting = Button(root, text = "기본 설정", # 핸드폰, 날씨
               font = ("한컴 고딕", 20), command= Mode_Basic_setting)
Basic_setting.place(relx=0.5, rely= 0.3, anchor='center')

global Study_settings
Study_settings = Button(root, text = "공부용 설정", # 핸드폰, 날씨, 배낭 가방
               font = ("한컴 고딕", 20), command= Mode_Study_settings)
Study_settings.place(relx=0.5, rely= 0.4, anchor='center')

global PC_room_setting
PC_room_setting = Button(root, text = "PC방용 설정", # 핸드폰, 날씨, 지갑
               font = ("한컴 고딕", 20), command= Mode_PC_room_setting)
PC_room_setting.place(relx=0.5, rely= 0.5, anchor='center')

global SCAN
SCAN = Button(root, text = "SCAN",
               font = ("Consolas", 40), command= destroy)
SCAN.place(relx=0.5, rely= 0.7, anchor='center')

hasnt_take = Label(root, text = "챙기지 않은 물건",
               font = ("Consolas", 30))

global detected
detected = Label(root, width=600, height=600)

have_to_take = ['person', 'cell phone']
is_continue_od = True



def videoCapture():
    ret, frame = cap.read()
    (image_np, detected_item) = scan_func(ret, frame)
    image = Image.fromarray(image_np)
    imgtk = ImageTk.PhotoImage(image=image)

    detected.config(image=imgtk)
    detected.image = imgtk

    dont_take = []

    for item in have_to_take:
        if item not in detected_item:
            dont_take.append(item)
    if len(dont_take) == 0:
        hasnt_take.configure(text='모든 물건을 챙겼음')
    else:
        hasnt_take.configure(text=', '.join(dont_take))
    
    if is_continue_od:
        root.after(10, videoCapture)

root.mainloop()