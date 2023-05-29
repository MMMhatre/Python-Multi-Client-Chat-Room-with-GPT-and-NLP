# -*- coding: utf-8 -*-
"""
Created on Sun May 21 20:22:50 2023

@author: malha
"""

import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import ImageTk, Image


# import sys
# from tkinter import ttk
# import tkinter
# from tkinter import font
# root = tkinter.Tk()
# fonts=list(font.families())
# fonts.sort()
# for i in fonts:
# 	print(i)

class myChatApp:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()


        self.login = Toplevel()
        self.login.title("Login Window")
        self.login.resizable(width=True, height=True)
        self.login.configure(width=1920, height=1080)

        img = ImageTk.PhotoImage(Image.open("bg2.jpg"))
        panel = Label(self.login, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        #self.login.wm_attributes('-transparentcolor', 'black')

        self.Label_Welcome_prompt = Label(self.login, text="Welcome to my chat application",
                                          justify=CENTER, font="Arial 40 bold",
                                          bg='#000000', fg='white')
        self.Label_Welcome_prompt.place(relwidth=0.6, relheight=0.09, relx=0.2, rely=0.12)


        self.Label_Login_prompt = Label(self.login, text="Enter your username",
                                        justify=CENTER, font="Arial 18",
                                        bg='#000000', fg='white')
        self.Label_Login_prompt.place(relheight=0.05, relx=0.2, rely=0.3)


        # self.Label_Name = Label(self.login, text="Name: ", font="Helvetica 20",
        #                         bg='black', fg='white')
        # self.Label_Name.place(relheight=0.05, relx=0.19, rely=0.35)


        self.Entry_Name = Entry(self.login, font="Helvetica 14")
        self.Entry_Name.place(relwidth=0.6, relheight=0.05, relx=0.2, rely=0.35)
        self.Entry_Name.focus()


        self.Label_Details_1 = Label(self.login, text="Python Project", font="Calibri 16", justify=CENTER,
                                     bg='#000000', fg='white')
        self.Label_Details_1.place(relwidth=0.15, relheight=0.02, relx=0.425, rely=0.92)

        # self.Label_Details_2 = Label(self.login, text="by Malhar Mhatre", font="Calibri 16", justify=CENTER,
        #                              bg='grey', fg='white')
        # self.Label_Details_2.place(relwidth=0.15, relheight=0.02, relx=0.425, rely=0.92)

        self.Label_Details_3 = Label(self.login, text="DBDA PRN 020", font="Calibri 16",justify=CENTER,
                                     bg='#000000', fg='white')
        self.Label_Details_3.place(relwidth=0.15, relheight=0.02, relx=0.425, rely=0.94)


        self.Button_Login = Button(self.login, text="LOG IN", font="Helvetica 24 bold",
                                   command=lambda: self.Login(self.Entry_Name.get()),
                                   bg='grey', fg='white', activebackground = 'red')
        self.Button_Login.place(relwidth=0.1, relheight=0.07, relx=0.45, rely=0.425)

        self.Window.mainloop()


    def Login(self,name):
        if len(name)==0:
            error = messagebox.showerror("INVALID NAME", "Enter a Valid Name")
            return
        self.AfterLogin(name)

    def VerifyLogin(self, uname, password):
        message = f"@Verify {name} {password}"
        client.send(message.encode('utf-8'))
        message = client.recv(1024).decode('utf-8')
        if "$Valid" in message:
            self.AfterLogin(name)
        else:
            return


    def AfterLogin(self, name):


        self.login.destroy()
        self.chat_GUI(name)

        rcv = threading.Thread(target=self.receiveMessages)
        rcv.start()

    def chat_GUI(self, name):
        self.name = name
        self.Window.deiconify()
        self.Window.title("Multi Client Chatroom")
        # self.Window.resizable(width=True, height=True)

        self.Window.configure(width=960, height=540, bg="#2A2C2E")

        self.Label_Head = Label(self.Window,
                               bg="#3C409C",
                               fg="#EAECEE",
                               text=f"Welcome to the chat room, {self.name}!",
                               font="Cascadia_Mono_Light 18")
        self.Label_Head.place(relwidth=1, relheight=0.08)

        self.Button_Exit = Button(self.Label_Head,
                                  text="EXIT",
                                  font="Arial_Black 16 bold",
                                  width=20,
                                  bg="#CC0202",
                                  activebackground="#FD830D",
                                  command = self.Quit)
        self.Button_Exit.place(relwidth=0.05, relheight=0.7,
                               relx=0.93, rely=0.1)



        self.Text_box = Text(self.Window,
                             width=20,
                             height=2,
                             bg="#17202A",
                             fg="#EAECEE",
                             font="Helvetica 16",
                             padx=5,
                             pady=5)

        self.Text_box.place(relheight=0.745,
                            relwidth=0.8,
                            relx=0.1,
                            rely=0.08)                                                                                  #self.Text_box.config(cursor="arrow")


        self.line_top = Label(self.Window, width=450, bg="#FD830D")
        self.line_top.place(relwidth=1, relheight=0.012, rely=0.07)

        # self.Button_ClearChat = Button(self.Label_Head,
        #                                text="CLEAR",
        #                                font="Arial_Black 16 bold",
        #                                width=20,
        #                                bg="#CC0202",
        #                                activebackground="#FD830D",
        #                                command = self.clearTextBox)
        # self.Button_ClearChat.place(relwidth=0.05, relheight=0.7,
        #                             relx=0.83, rely=0.1)

        #img = ImageTk.PhotoImage(Image.open("bg1.jpg"))
        #panel = Label(self.Text_box, image = img)
        #panel.pack(side = "bottom", expand = "yes")


        self.Label_Bottom = Label(self.Window,
                                  bg="#2D3748",
                                  height=40)
        self.Label_Bottom.place(relwidth=1, rely=0.825)


        self.Entry_Message = Entry(self.Label_Bottom, bg="#2C3E50", fg="#EAECEE",
                                   font="Helvetica 16")
        self.Entry_Message.place(relwidth=0.74,
                                 relheight=0.06,
                                 relx=0.011,
                                 rely=0.04)
        self.Entry_Message.focus()


        self.Button_Send = Button(self.Label_Bottom,
                                  text="SEND ⇨",
                                  font = "Arial_Black 18 bold",
                                  width=20,
                                  bg="#607FF2",
                                  activebackground="#FD830D",
                                  command=lambda: self.sendButton(self.Entry_Message.get()))
        self.Button_Send.place(relwidth=0.22, relheight=0.06,
                               relx=0.77, rely=0.04)

        scrollbar = Scrollbar(self.Text_box)
        scrollbar.place(relwidth=0.015, relheight=1, relx=0.985)

        scrollbar.config(command=self.Text_box.yview)

        self.line_bottom = Label(self.Window, width=450, bg="#FD830D")
        self.line_bottom.place(relwidth=1, relheight=0.012, rely=0.825)

        self.Text_box.config(state=DISABLED)

    # def clearTextBox(self):
    #     self.Text_box.delete(1.0,END)
    def Quit(self):
        Yes = messagebox.askyesno("Close Chatroom", "Are you sure if you wish to close this window")
        if Yes:
            self.Window.destroy()
        return

    def sendButton(self, msg):
        self.Text_box.config(state=DISABLED)
        self.msg = msg
        self.Entry_Message.delete(0, END)
        sendThread = threading.Thread(target=self.sendMessage)
        sendThread.start()

    def receiveMessages(self):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == 'NAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    self.Text_box.config(state=NORMAL)
                    self.Text_box.insert(END, message+"\n")
                    self.Text_box.config(state=DISABLED)
                    self.Text_box.see(END)
            except:
                print("ERROR")
                client.close()
                break

    def sendMessage(self):
        self.Text_box.config(state=DISABLED)
        while True:
            message = (f"  {self.name}: {self.msg}")
            if ("@exit" in message.casefold()):
                #client.close()
                self.Window.destroy()
            else:
                client.send(message.encode('utf-8'))
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("192.168.43.117", 5000))
    c = myChatApp()