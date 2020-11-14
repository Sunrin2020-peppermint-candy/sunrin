from tkinter import *

root = Tk()
root.title("물건 챙김 알리미")
root.geometry("600x900")
root.resizable(False, False)

def Scan_destroy():
    Basic.destroy()
    SCAN.destroy()

def Scan():
    global SCAN
    SCAN = Button(root, text = "SCAN",
               font = ("Consolas", 50), command= Scan_destroy)
    SCAN.place(relx=0.5, rely= 0.5, anchor='center')

def destroy():
    Label1.destroy()
    Button1.destroy()
    Button2.destroy()
    Button3.destroy()
    Button4.destroy()

def Basic_setting():
    destroy()
    global Basic
    Basic = Label(root, text = "기본 설정",
               font = ("한컴 고딕", 30))
    Basic.place(relx=0.5, rely= 0.2, anchor='center')
    Scan()
    
def Study_settings():
    destroy()
    global Basic
    Basic = Label(root, text = "공부용 설정",
               font = ("한컴 고딕", 30))
    Basic.place(relx=0.5, rely= 0.2, anchor='center')
    Scan()

def PC_room_setting():
    destroy()
    global Basic
    Basic = Label(root, text = "PC방용 설정",
               font = ("한컴 고딕", 30))
    Basic.place(relx=0.5, rely= 0.2, anchor='center')
    Scan()
    
def Settings_for_users():
    destroy()
    global Basic
    Basic = Label(root, text = "사용자용 설정",
               font = ("한컴 고딕", 30))
    Basic.place(relx=0.5, rely= 0.2, anchor='center')
    Scan()

    

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
