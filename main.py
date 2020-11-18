from tkinter import *

import weather

from PIL import ImageTk
from PIL import Image

from scan import scan_func

import cv2

MODE = {
    1: {"name": "기본 설정", "items": ["face mask", "cell phone"]},
    2: {"name": "공부용 설정", "items": ["face mask", "cell phone", "backpack"]},
    3: {"name": "PC방용 설정", "items": ["face mask", "cell phone", "wallet"]},
}

root = Tk()
root.title("물건 챙김 알리미")
root.geometry("600x900")
root.resizable(False, False)


title_label = Label(root, text="물건챙김 알리미", font=("나눔스퀘어 ExtraBold", 40))
title_label.place(relx=0.5, rely=0.15, anchor="center")

mode_setting = 1
mode_label = Label(root, text="MODE: {}".format(MODE[1]["name"]), font=("나눔스퀘어", 15))
mode_label.place(relx=0.5, rely=0.9, anchor="center")


def gotoScanPage():
    title_label.place_forget()
    mode_label.place_forget()
    basic_setting_btn.place_forget()
    study_setting_btn.place_forget()
    pc_room_setting_btn.place_forget()
    scan_btn.place_forget()

    global cap
    cap = cv2.VideoCapture(0)

    global have_to_take_now
    have_to_take_now = MODE[mode_setting]["items"]
    if weather.is_umbrella_required():
        have_to_take_now.append("umbrella")

    print(have_to_take_now)

    detected.place(relx=0.5, rely=0.2, anchor="center")
    hasnt_take_label.place(relx=0.5, rely=0.6, anchor="center")
    hasnt_take_items_label.place(relx=0.5, rely=0.7, anchor="center")
    go_home_btn.place(relx=0.5, rely=0.9, anchor="center")

    global is_continue_od
    is_continue_od = True

    videoCapture()


def gotoHomePage():
    detected.place_forget()
    hasnt_take_label.place_forget()
    hasnt_take_items_label.place_forget()
    go_home_btn.place_forget()

    global is_continue_od
    is_continue_od = False

    title_label.place(relx=0.5, rely=0.15, anchor="center")
    basic_setting_btn.place(relx=0.5, rely=0.3, anchor="center")
    study_setting_btn.place(relx=0.5, rely=0.4, anchor="center")
    pc_room_setting_btn.place(relx=0.5, rely=0.5, anchor="center")
    scan_btn.place(relx=0.5, rely=0.7, anchor="center")
    mode_label.place(relx=0.5, rely=0.9, anchor="center")


def set_mode(mode_id):
    global mode_setting
    mode_setting = mode_id
    mode_label.config(text="MODE: {}".format(MODE[mode_id]["name"]))


basic_setting_btn = Button(
    root, text=MODE[1]["name"], font=("나눔스퀘어", 20), command=lambda: set_mode(1)
)
basic_setting_btn.place(relx=0.5, rely=0.3, anchor="center")

study_setting_btn = Button(
    root, text=MODE[2]["name"], font=("나눔스퀘어", 20), command=lambda: set_mode(2)
)
study_setting_btn.place(relx=0.5, rely=0.4, anchor="center")

pc_room_setting_btn = Button(
    root, text=MODE[3]["name"], font=("나눔스퀘어", 20), command=lambda: set_mode(3)
)
pc_room_setting_btn.place(relx=0.5, rely=0.5, anchor="center")

scan_img = PhotoImage(file="icon.png")
scan_btn = Button(root, image=scan_img, font=("나눔스퀘어", 40), command=gotoScanPage)
scan_btn.place(relx=0.5, rely=0.7, anchor="center")

go_home_btn = Button(root, text="돌아가기", font=("나눔스퀘어", 20), command=gotoHomePage)

hasnt_take_label = Label(root, text="", font=("나눔스퀘어 Bold", 25))
hasnt_take_items_label = Label(root, text="챙기지 않은 물건", font=("나눔스퀘어", 15))

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
        hasnt_take_label.configure(text="필요한 모든 물건을 챙겼습니다!")
        hasnt_take_items_label.configure(text="")
    else:
        hasnt_take_label.configure(text="다음 물건들을 챙겨야 합니다!\n")
        hasnt_take_items_label.configure(text=", ".join(dont_take))

    if is_continue_od:
        root.after(10, videoCapture)
    else:
        cap.release()


root.mainloop()
