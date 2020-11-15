from tkinter import *

import weather

from PIL import ImageTk
from PIL import Image

from scan import scan_func

import cv2

HAVE_TO_TAKE = {
    1: ['face_mask', 'cell phone'],
    2: ['face_mask', 'cell phone', 'backpack'],
    3: ['face_mask', 'cell phone', 'wallet'],
}

root = Tk()
root.title("물건 챙김 알리미")
root.geometry("600x900")
root.resizable(False, False)


Label_stuff= Label(root, text = "물건챙김 알리미",
               font = ("나눔스퀘어 ExtraBold", 40))
Label_stuff.place(relx=0.5, rely= 0.15, anchor='center')

Mode_setting = 1
Mode = Label(root, text = "MODE: 기본설정",
               font = ("나눔스퀘어", 15))
Mode.place(relx=0.5, rely= 0.9, anchor='center')

def gotoScanPage():
    Label_stuff.place_forget()
    Mode.place_forget()
    Basic_setting.place_forget()
    Study_settings.place_forget()
    PC_room_setting.place_forget()
    SCAN.place_forget()

    global cap
    cap = cv2.VideoCapture(0)

    print('mode: ', Mode_setting)
    global have_to_take_now
    have_to_take_now = HAVE_TO_TAKE[Mode_setting]
    if weather.is_umbrella_required():
        have_to_take_now.append('umbrella')

    print(have_to_take_now)

    detected.place(relx=0.5, rely= 0.2, anchor='center')
    hasnt_take.place(relx=0.5, rely= 0.6, anchor='center')
    hasnt_take_items.place(relx=0.5, rely= 0.7, anchor='center')
    goHome.place(relx=0.5, rely= 0.9, anchor='center')

    global is_continue_od
    is_continue_od = True
    videoCapture()

def gotoHomePage():
    detected.place_forget()
    hasnt_take.place_forget()
    hasnt_take_items.place_forget()
    goHome.place_forget()

    global is_continue_od
    is_continue_od = False

    Label_stuff.place(relx=0.5, rely= 0.15, anchor='center')
    Basic_setting.place(relx=0.5, rely= 0.3, anchor='center')
    Study_settings.place(relx=0.5, rely= 0.4, anchor='center')
    PC_room_setting.place(relx=0.5, rely= 0.5, anchor='center')
    SCAN.place(relx=0.5, rely= 0.7, anchor='center')
    Mode.place(relx=0.5, rely= 0.9, anchor='center')

def Mode_Basic_setting():
    Mode.config(text="MODE: 기본설정")
    global Mode_setting
    Mode_setting = 1

def Mode_Study_settings():
    Mode.config(text="MODE: 공부용 설정")
    global Mode_setting
    Mode_setting = 2

def Mode_PC_room_setting():
    Mode.config(text="MODE: PC방용 설정")
    global Mode_setting
    Mode_setting = 3

global Basic_setting
Basic_setting = Button(root, text = "기본 설정", # 핸드폰, 날씨
               font = ("나눔스퀘어", 20), command= Mode_Basic_setting)
Basic_setting.place(relx=0.5, rely= 0.3, anchor='center')

global Study_settings
Study_settings = Button(root, text = "공부용 설정", # 핸드폰, 날씨, 배낭 가방
               font = ("나눔스퀘어", 20), command= Mode_Study_settings)
Study_settings.place(relx=0.5, rely= 0.4, anchor='center')

global PC_room_setting
PC_room_setting = Button(root, text = "PC방용 설정", # 핸드폰, 날씨, 지갑
               font = ("나눔스퀘어", 20), command= Mode_PC_room_setting)
PC_room_setting.place(relx=0.5, rely= 0.5, anchor='center')

scan_img = Image.open("icon.jpg")
scan_photo = ImageTk.PhotoImage(scan_img)

global SCAN
SCAN = Button(root, image=scan_photo,
               font = ("나눔스퀘어", 40), command=gotoScanPage)
SCAN.place(relx=0.5, rely= 0.7, anchor='center')

global goHome
goHome = Button(root, text = "돌아가기",
               font = ("나눔스퀘어", 20), command=gotoHomePage)

hasnt_take = Label(root, text = "챙기지 않은 물건이 있습니다!",
               font = ("나눔스퀘어 Bold", 15))
hasnt_take_items = Label(root, text = "챙기지 않은 물건",
               font = ("나눔스퀘어", 15))

global detected
detected = Label(root, width=600, height=600)

is_continue_od = True



def videoCapture():
    ret, frame = cap.read()
    (image_np, detected_item) = scan_func(ret, frame)
    image = Image.fromarray(image_np)
    imgtk = ImageTk.PhotoImage(image=image)

    detected.config(image=imgtk)
    detected.image = imgtk

    dont_take = []

    for item in have_to_take_now:
        if item not in detected_item:
            dont_take.append(item)
    if len(dont_take) == 0:
        hasnt_take.configure(text='모든 물건을 챙겼습니다!')
        hasnt_take_items.configure(text='')
    else:
        hasnt_take.configure(text='다음 물건들을 챙기지 않았습니다!\n')
        hasnt_take_items.configure(text=', '.join(dont_take))
    
    if is_continue_od:
        root.after(10, videoCapture)
    else:
        cap.release()

root.mainloop()