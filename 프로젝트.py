from tkinter import *

root = Tk()
root.title("물건 챙김 알리미")
root.geometry("600x900")
root.resizable(False, False)

Label1 = Label(root, text = "물건챙김 알리미",
               font = ("한컴 고딕", 30))
Label1.place(relx=0.5, rely= 0.2, anchor='center')



Button1 = Button(root, text = "기본설정",
                 font = ("한컴 고딕", 20))
Button1.place(relx=0.5, rely= 0.4, anchor='center')

Button2 = Button(root, text = "공부용 설정",
                 font = ("한컴 고딕", 20))
Button2.place(relx=0.5, rely= 0.5, anchor='center')

Button3 = Button(root, text = "PC방용 설정",
                 font = ("한컴 고딕", 20))
Button3.place(relx=0.5, rely= 0.6, anchor='center')

Button4 = Button(root, text = "사용자용 설정",
                 font = ("한컴 고딕", 20))
Button4.place(relx=0.5, rely= 0.7, anchor='center')



root.mainloop()
