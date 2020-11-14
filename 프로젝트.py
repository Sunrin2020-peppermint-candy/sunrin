from tkinter import *

from PIL import ImageTk
from PIL import Image

from scan import scan_func

import cv2

cap = cv2.VideoCapture(0)

root = Tk()
root.title("물건 챙김 알리미")
root.geometry("600x900")
root.resizable(False, False)

have_to_take = ['person', 'cell phone']

def videoCapture():
    ret, frame = cap.read()
    (image_np, detected_item) = scan_func(ret, frame)
    image = Image.fromarray(image_np)
    imgtk = ImageTk.PhotoImage(image=image)

    detected.config(image=imgtk)
    detected.image = imgtk

    detected_list.configure(text=', '.join(detected_item))

    dont_take = []

    for item in have_to_take:
        if item not in detected_item:
            dont_take.append(item)
    if len(dont_take) == 0:
        detected_list.configure(text='모든 물건을 챙겼음')
    else:
        detected_list.configure(text=', '.join(dont_take))
    
    root.after(10, videoCapture)

def Basic_setting():
    Label1.destroy()
    Button1.destroy()
    Button2.destroy()
    Button3.destroy()
    Button4.destroy()
    Basic = Label(root, text = "기본 설정",
               font = ("한컴 고딕", 30))
    Basic.place(relx=0.5, rely= 0.2, anchor='center')
    SCAN = Button(root, text = "SCAN",
               font = ("Consolas", 50))
    SCAN.place(relx=0.5, rely= 0.5, anchor='center')

    global detected
    detected = Label(root, width=600, height=600)
    detected.place(relx=0.5, rely= 0.2, anchor='center')
    global detected_list
    detected_list = Label(root, text = "챙긴물건",
                                font = ("한컴 고딕", 30))
    
    detected_list.place(relx=0.5, rely= 0.5, anchor='center')

    videoCapture()
 
    
def Study_settings():
    Label1.destroy()
    Button1.destroy()
    Button2.destroy()
    Button3.destroy()
    Button4.destroy()
    Basic = Label(root, text = "공부용 설정",
               font = ("한컴 고딕", 30))
    Basic.place(relx=0.5, rely= 0.2, anchor='center')
    SCAN = Button(root, text = "SCAN",
               font = ("Consolas", 50))
    SCAN.place(relx=0.5, rely= 0.5, anchor='center')

def PC_room_setting():
    Label1.destroy()
    Button1.destroy()
    Button2.destroy()
    Button3.destroy()
    Button4.destroy()
    Basic = Label(root, text = "PC방용 설정",
               font = ("한컴 고딕", 30))
    Basic.place(relx=0.5, rely= 0.2, anchor='center')
    SCAN = Button(root, text = "SCAN",
               font = ("Consolas", 50))
    SCAN.place(relx=0.5, rely= 0.5, anchor='center')
    
def Settings_for_users():
    Label1.destroy()
    Button1.destroy()
    Button2.destroy()
    Button3.destroy()
    Button4.destroy()    
    Basic = Label(root, text = "사용자용 설정",
               font = ("한컴 고딕", 30))
    Basic.place(relx=0.5, rely= 0.2, anchor='center')
    SCAN = Button(root, text = "SCAN",
               font = ("Consolas", 50))
    SCAN.place(relx=0.5, rely= 0.5, anchor='center')

    

Label1 = Label(root, text = "물건챙김 알리미",
               font = ("한컴 고딕", 30))
Label1.place(relx=0.5, rely= 0.2, anchor='center')


Button1 = Button(root, text = "기본설정",
                 font = ("한컴 고딕", 20), command= Basic_setting)
Button1.place(relx=0.5, rely= 0.4, anchor='center')

Button2 = Button(root, text = "공부용 설정",
                 font = ("한컴 고딕", 20), command= Study_settings)
Button2.place(relx=0.5, rely= 0.5, anchor='center')

Button3 = Button(root, text = "PC방용 설정",
                 font = ("한컴 고딕", 20), command= PC_room_setting)
Button3.place(relx=0.5, rely= 0.6, anchor='center')

Button4 = Button(root, text = "사용자용 설정",
                 font = ("한컴 고딕", 20), command= Settings_for_users)
Button4.place(relx=0.5, rely= 0.7, anchor='center')



root.mainloop()
