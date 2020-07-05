from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวณเลข')
GUI.geometry('800x700')
# toplv


def math_additional():
    GUI2 = Toplevel()
    GUI2.title('หน้าต่างคณิตศาสตร์')
    GUI2.geometry('500x400')

    def Add():
        messagebox.showinfo('การบวก', 'ตัวอย่าง: 1+ 1 = 2')

    img_B1 = PhotoImage(file='B1.png')
    logo = ttk.Label(GUI2, text='Basic Calculation', font=FONT, image=img_B1)
    logo.pack()

    B2 = Button(GUI2, text='ตัวอย่างการบวกเลข', command=Add, font=('Angsana', 16))
    B2.pack()

    GUI2.mainloop()


# toplv
# menu
menubar = Menu(GUI)
GUI.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Exit', command=GUI.quit)
menubar.add_cascade(label='File', menu=filemenu)

mathmenu = Menu(menubar, tearoff=0)
mathmenu.add_command(label='การบวก', command=math_additional)
mathmenu.add_command(label='การลบ')
mathmenu.add_command(label='การคูณ')
mathmenu.add_command(label='การหาร')

menubar.add_cascade(label='คณิตศาสตร์', menu=mathmenu)

# menu
FONT = ('AngsanaUPC', 16, 'bold')


def AAA():
    aaa = int(result1.get())
    bbb = int(result2.get())
    ccc = int(result3.get())
    total = aaa*bbb*ccc

    showRes.set(f'ผลลัพธ์เท่ากับ {total} ลบ.ม.')


# TAB
Tab = ttk.Notebook(GUI)

T1 = Frame(Tab)
T2 = Frame(Tab)


Tab.pack(fill=BOTH, expand=1)

Tab.add(T1, text='BEAM')
Tab.add(T2, text='บวกไปเรื่อยๆ')
# TAB

F1 = Frame(T1)
F1.pack()

img_B1 = PhotoImage(file='B1.png')
img1 = ttk.Label(F1, text='Basic Calculation', font=FONT,
                 image=img_B1, compound='bottom')
img1.grid(row=1, column=0, pady=10)


result1 = StringVar()
result2 = StringVar()
result3 = StringVar()
showRes = StringVar()

L01 = ttk.Label(F1, text='กว้าง(ม.) :')
L01.grid(row=2, column=0, padx=20)

E1 = Entry(F1, textvariable=result1, font=FONT)
E1.grid(row=3, column=0)

L02 = ttk.Label(F1, text='ยาว(ม.) :')
L02.grid(row=4, column=0, padx=20)

E2 = Entry(F1, textvariable=result2, font=FONT)
E2.grid(row=5, column=0)

L03 = ttk.Label(F1, text='สูง(ม.) :')
L03.grid(row=6, column=0, padx=20)

E3 = Entry(F1, textvariable=result3, font=FONT)
E3.grid(row=7, column=0)

B1 = ttk.Button(F1, text='Press the button', command=AAA)
B1.grid(row=8, column=0, pady=20)

L2 = Label(F1, textvariable=showRes, font=FONT)
L2.grid(row=9, column=0)

###################################################


def pluss():
    y = []
    for i in range(1, int(result.get())+1):
        y.append(i)
        sumy = sum(y)
        leny = len(y)
    showRess.set(f'บวก 1 ถึง {leny} เท่ากับ {sumy}')


Le1 = Label(T2, text='บวกไปเรื่อยๆ', font=('Angsana', 16))
Le1.pack(pady=20)  # pading แกน y 20 px

result = StringVar()
showRess = StringVar()

Ee1 = Entry(T2, textvariable=result, font=('Angsana', 16))
Ee1.pack()

Be1 = Button(T2, text='Press the button', fg='white',
             bg='black', command=pluss, font=('Angsana', 16))
Be1.pack(pady=20)

Le2 = Label(T2, textvariable=showRess, font=('Angsana', 16))
Le2.pack()

GUI.mainloop()
