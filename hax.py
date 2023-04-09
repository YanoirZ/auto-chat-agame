import time
import pyautogui as pt
import keyboard
from tkinter import *
import tkinter as tk
from threading import Thread
import functools
import pyperclip
import keyboard
from tkinter import ttk
from tkinter import filedialog
import random
import pickle
import os

active_counter=0

def follow(thefile):
  thefile.seek(0,2)
  while True:
    line = thefile.readline()
    if not line:
      time.sleep(0.1)
      continue
    yield line

def start_stop():
    global active_counter
    if button['text'] == 'Start':
        active_counter = 0
        sta = Thread(target = run)
        sta.start()
        button.config(text="Stop", bg="red", activebackground="red")
    else:
        active_counter = 1
        button.config(text="Start", bg="light green", activebackground="light green")

def do_not_run_twice(func):
    prev_call = None

    @functools.wraps(func) # It is good practice to use this decorator for decorators
    def wrapper(*args, **kwargs):
        nonlocal prev_call
        if (args, kwargs) == prev_call:
            return None
        prev_call = args, kwargs
        return func(*args, **kwargs)
    return wrapper

@do_not_run_twice    
def auto(pkm,t):
    lAnswer.configure(text=pkm.lower())
    pyperclip.copy(pkm.lower())
    keyboard.press_and_release('t')
    time.sleep(t)
    keyboard.press_and_release('ctrl+a')
    time.sleep(0.05)
    keyboard.press_and_release('ctrl+v')
    if t<2.5:
      time.sleep(1)
      keyboard.press_and_release('enter')
    else:
      keyboard.press_and_release('enter')
    time.sleep(3)

def chayngaydi():
    chay=Thread(target=click)
    chay.start()

def click():
    global active_counter
    tam=active_counter
    time.sleep(4)
    mon=float(tClick.get())
    if boss.get()==1:
        active_counter=1
    if check.get()==1:
        if cb1.get()=='Righ Click':
            while (not keyboard.is_pressed('`')) and check.get()==1:
                pt.rightClick(interval=mon)
        else:
            while (not keyboard.is_pressed('`')) and check.get()==1:
                pt.leftClick(interval=mon)
        check.set(0)
        active_counter=tam
    if active_counter ==0:
      sta = Thread(target = run)
      sta.start()

def clickAFK():
    time.sleep(4)
    if vAFK.get()==1:
        while (not keyboard.is_pressed('`')) and vAFK.get()==1:
            a=random.randint(60, 300)
            pt.leftClick(interval=a)
        vAFK.set(0)

def afk():
    AFK=Thread(target=clickAFK)
    AFK.start()


def run():
    dex=float(tdex.get())
    unr=float(tUnscramble.get())
    q5=float(tQuest5.get())
    q6=float(tQuest.get())
    f = open(r"Pokedex.txt",'r')
    a = f.read().splitlines()
    q=open(r"h-tl.txt",'r')
    quest=q.read().splitlines()
    logfile = open(log_path,'r')
    loglines = follow(logfile)
    for line in loglines:
      if active_counter==1:
        break
      if "[Chat Games]" in line:

        if " dex number" in line:
          i=-3
          m=1
          pkm=0
          while line[i] != ' ':
            if line[i] in {'0','1','2','3','4','5','6','7','8','9'}:
              pkm = pkm + int((line[i]))*m
              i-=1
              m=m*10
          auto((a[pkm-1]),len(a[pkm-1])*dex+1.2145)
          
        if "Unscramble the word" in line:
          i=-2
          pkm=''
          while line[i] != ' ':
            pkm = pkm + (line[i])
            i-=1
          for p in a:
            if len(pkm) == len(p):
              x=p.lower()
              cc= len( set(x) & set(pkm) )
              if cc == len(set(x)):
                l1=sorted(pkm)
                l2=sorted(x)
                if l1==l2:
                  if len(x)<5:
                    auto(x,len(x)*unr)
                  elif len(x)<=9:
                    auto(x,len(x)*(unr+0.111))
                  else:
                    auto(x,len(x)*(unr+0.211))

        # if 'Click the' in line:
        #     pt.press('t')
        #     if ' red' in line:
        #       clickbt = pt.locateCenterOnScreen('red.jpg',region=(0,0,1920,1080),grayscale=True,confidence=0.6)
        #       if clickbt is not True:
        #           pt.moveTo(clickbt)
        #           click()
        #       elif 'green' in line:
        #         clickbt = pt.locateCenterOnScreen('green.jpg',region=(0,0,1920,1080),grayscale=True,confidence=0.6)
        #         if clickbt is not True:
        #           pt.moveTo(clickbt)
        #           click()
        #       else:
        #         clickbt = pt.locateCenterOnScreen('white.jpg',region=(0,0,1920,1080),grayscale=True,confidence=0.6)
        #         if clickbt is not True:
        #           pt.moveTo(clickbt)
        #           click()

        #     pt.click(784,565)
        #     time.sleep(0.5)
        #     pt.press('Enter')

        else:
          d=0
          for i in quest:
            if d%2 == 0:
              if i !='':
                traloi=i.lower()
                cauhoi=line.lower()
                if traloi in cauhoi:
                  if (d+1)%2 !=0:
                    if len(quest[d+1])<6:
                      auto(quest[d+1].lower(),q5)
                    else:
                        auto(quest[d+1].lower(),len(quest[d+1])*q6+0.456)
            d+=1
      if 'It got away!' in line:
        time.sleep(0.3254)
        pt.rightClick()


window=Tk()
window.title("Yanoo's Program")
# window.iconbitmap(r"yano.ico")

#label
ldex=Label(window,text='Dex Number: ',font=('Arial',15))
ldex.grid(column=0,row=1)
lUnscramble=Label(window,text='Unscramble: ',font=('Arial',15))
lUnscramble.grid(column=0,row=2)

lQuest5=Label(window,text='Quest < 5: ',font=('Arial',15))
lQuest5.grid(column=0,row=3)

lQuest=Label(window,text='Quest > 5: ',font=('Arial',15))
lQuest.grid(column=0,row=4)

lAnswer=Label(window,text='Answer',font=('Arial',20))
lAnswer.grid(column=0,row=5)

lClick=Label(window,text='time: ',font=('Arial',15))
lClick.grid(column=0,row=7)

#text box
tdex=Entry(window,width=20)
tdex.insert(END,0.324)
tdex.grid(row=1,column=1,ipady=1,ipadx=1)

tUnscramble=Entry(window,width=20)
tUnscramble.insert(END,0.244)
tUnscramble.grid(column=1,row=2)

tQuest5=Entry(window,width=20)
tQuest5.insert(END,1.657)
tQuest5.grid(column=1,row=3)

tQuest=Entry(window,width=20)
tQuest.insert(END,0.234)
tQuest.grid(column=1,row=4)

tClick=Entry(window,width=20)
tClick.insert(END,0.1)
tClick.grid(column=1,row=7)

#button
button = tk.Button(text="Start", bg="light green", bd=0, highlightthickness=0,
                                    activebackground="light green", command=start_stop)
button.grid(row=0, column=0,columnspan=4, sticky="nswe")


#check box
check = tk.IntVar()
boss=tk.IntVar()
vAFK=tk.IntVar()
c1 = tk.Checkbutton(window, text='AutoClick',variable=check, onvalue=1, offvalue=0, command=chayngaydi)
c1.grid(column=0,row=6)

c2=tk.Checkbutton(window, text='Boss?',variable=boss, onvalue=1, offvalue=0)
c2.grid(column=1,row=6)

Cafk=Checkbutton(window,text='AFK Mode',variable=vAFK, onvalue=1, offvalue=0,command=afk)
Cafk.grid(column=0,row=8, sticky = EW,columnspan=4)


#combo box
idk = tk.StringVar()
cb1=ttk.Combobox(window,width=10,textvariable = idk)
cb1['values'] = ('Righ Click','Left Click')
cb1.grid(column=3,row =6)
cb1.current(0)

idk = tk.StringVar()
cb1=ttk.Combobox(window,width=10,textvariable = idk)
cb1['values'] = ('Righ Click','Left Click')
cb1.grid(column=3,row =6)
cb1.current(0)

# Hàm lưu giá trị đường dẫn vào file `last_path.txt`
def save_last_path(path):
    with open('last_path.txt', 'w') as f:
        f.write(path)


# Hàm đọc giá trị đường dẫn cuối cùng từ file `last_path.txt`
def read_last_path():
    if os.path.isfile('last_path.txt'):
        with open('last_path.txt', 'r') as f:
            return f.read()
    else:
        return ''



# Tạo biến lưu giá trị đường dẫn
last_path = tk.StringVar(value=read_last_path())
log_path=read_last_path()
# Tạo hàm mở hộp thoại để chọn đường dẫn
def open_file_dialog():
    path = filedialog.askopenfilename(
        title='Chọn file .log',
        filetypes=[('Log files', '*.log')]
    )
    if path:
        last_path.set(path)
        save_last_path(path)

# Tạo nút mở hộp thoại
buttonBrowse = tk.Button(window, text="Browse", command=open_file_dialog)
buttonBrowse.grid(column=0,row=9)

# Tạo ô hiển thị đường dẫn đã chọn
path_entry = tk.Entry(window, textvariable=last_path, state="readonly")
path_entry.grid(column=1, row=9, columnspan=2, sticky="EW")




window.mainloop()
