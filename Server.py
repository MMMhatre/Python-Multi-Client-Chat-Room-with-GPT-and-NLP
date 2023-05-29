# -*- coding: utf-8 -*-
"""
Created on Sun May 21 18:15:07 2023

@author: malha
"""

import re
import openai
import time
import mysql.connector as m
mydatabase=m.connect(host="localhost",user="root",password="Ycqbe1000",database="pythondb1")
cursor=mydatabase.cursor()

Query_INSERT_Client_table = "INSERT INTO Client_table_2(name, ip) VALUES(%s, %s);"
Query_INSERT_Message_table = "INSERT INTO Message_table_2(name, message) VALUES(%s, %s);"
Query_SELECT_Message_table = "SELECT message FROM Message_table_2"

messages=[]

with open('API_key.txt','r') as f:
    a=f.read()
openai.api_key = a

def startChat():
    print("server is working on " + IPv4_address)
    server.listen()

    while True:
        client_obj, client_ip = server.accept()

        client_obj.send("NAME".encode('utf-8'))

        client_name = client_obj.recv(1024).decode('utf-8')

        client_ip_list.append(client_obj)
        client_name_list.append(client_name)
        cursor.execute(Query_INSERT_Client_table, [str(client_name),str(client_ip[0])])
        mydatabase.commit()

        cursor.execute(Query_SELECT_Message_table)
        msg_list = list(cursor.fetchall())
        for i in msg_list:
            time.sleep(0.05)
            client_obj.send(i[0].encode('utf-8'))

        print(f"The Client's name is : {client_name}")

        SendtoAll(f"  {client_name} has joined the chat!".encode('utf-8'))

        client_obj.send('  Connection successful!'.encode('utf-8'))

        thread = threading.Thread(target = incoming_msg, args = (client_obj, client_ip, client_name))
        thread.start()

        print("Active connections = {}".format(threading.active_count()-1))

        #thread.join()
        #if (threading.active_count()-1)==0:
        #    break
    print("Ending the Program")

def Verify(msg):
    # FORMAT = "@Verify {uname} {password}"
    pass

def AddUser(msg):
    # FORMAT = "@AddUser {uname} {password}"
    pass

def RemoveUser(msg):
    # FORMAT = "@RemoveUser {uname} {password}"
    pass

def DelChat(msg):
    # FORMAT = "@DelChat {uname}"
    pass

def Bot(msg):
    # FORMAT = "@Bot {text}"
    index = msg.index('@bot')+4
    message = msg[index:]
    messages.append({"role": "user", "content": message})
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    msg = f"  ChatGPT: {reply}"
    messages.append({"role": "assistant", "content": reply})
    # cursor.execute(Query_INSERT_Message_table, ["ChatGPT",msg])
    # mydatabase.commit()

    SendtoAll(msg.encode('utf-8'))

def Intercept_Incoming_Messages(client_obj, client_ip, client_name):
    while True:
        try:
            message = client_obj.recv(1024)
            msg = (message.decode()).casefold()
            if ("@Verify" in msg):
                Verify(msg)
            elif ("@addUser" in msg):
                AddUser(msg)
            elif ("@removeUser" in msg):
                RemoveUser(msg)
            elif ("@delChat" in msg):
                DelChat(msg)
            elif ("@bot" in msg):
                Bot(msg)
            else:
                SendtoAll(message)
                cursor.execute(Query_INSERT_Message_table, [str(client_name),str(msg)])
                mydatabase.commit()
        except ConnectionResetError:
            print("Connection Terminated for {} at IPv4 {}".format(client_name, client_ip))
            break

def incoming_msg(client_obj, client_ip, client_name):
    print(f"New connection for {client_name} at {client_ip} established")

    while True:
        try:
            message = client_obj.recv(1024)

            msg = message.decode()

            if("@exit" in msg.casefold()):
                break
            SendtoAll(message)
            # print(type(msg),msg)
            # re_match = re.match(r'@bot',msg.casefold())
            # if re_match:
            #     print("MATCH")
            #     mytuple = re_match.span()
            #     SendtoAll(msg[mytuple[-1]:])

            cursor.execute(Query_INSERT_Message_table, [str(client_name),str(msg)])
            mydatabase.commit()

            if "@bot" in msg:
                index = msg.index('@bot')+4
                message = msg[index:]
                messages.append({"role": "user", "content": message})
                chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
                reply = chat.choices[0].message.content
                msg = f"  ChatGPT: {reply}"
                messages.append({"role": "assistant", "content": reply})
                cursor.execute(Query_INSERT_Message_table, ["ChatGPT",msg])
                mydatabase.commit()

                SendtoAll(msg.encode('utf-8'))
        except ConnectionResetError:
            print("Connection Terminated for {} at IPv4 {}".format(client_name, client_ip))
            break
    print(f"Ending connection with {client_ip}")
    print("Active connections = {}".format(threading.active_count()-2))
    # client_obj.close()

def SendtoAll(message):
    for client in client_ip_list:
        client.send(message)

import socket
import threading

IPv4_address = socket.gethostbyname(socket.gethostname())
client_ip_list, client_name_list = [], []

# AF_INET Address Family  IPv4  32bit 2^8 4times
# AF_INET6 Address Family IPv6 128bit 8*(4*4hex)
# SOCK_STREAM connection oriented TCP(Transmission Control Proctocol)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((IPv4_address, 5000))
    startChat()


# import tkinter
# from tkinter import font
# root = tkinter.Tk()
# fonts=list(font.families())
# fonts.sort()
# for i in fonts:
# 	print(i)




