# coding:utf-8
# author: Meditator_hkx
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a hello world GUI example.'

# from Tkinter import *
# import tkMessageBox
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         tkMessageBox.showinfo('Message', 'Hello, %s' % name)
#
# app = Application()
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()

from Tkinter import Tk, Label, Button, Entry, Text, IntVar, StringVar, END, W, E
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

class Automailor:
    def __init__(self, master):
        self.master = master
        master.title("AutoMailor")

        # Guest object
        self.guest = Guest()

        # self.total = 0
        # self.entered_number = 0
        #
        # self.total_label_text = IntVar()
        # self.total_label_text.set(self.total)
        #
        # Change words while click "Run" button
        self.my_text = StringVar()
        self.my_text.set("Hello, master!")
        self.my_label = Label(master, textvariable = self.my_text)
        #
        # self.total_label = Label(master, textvariable=self.total_label_text)
        # self.label = Label(master, text="Total:")

        # Label Added
        self.account_label = Label(master, text = "Sender account: ")
        self.pwd_label = Label(master, text = "Sender password: ")
        self.port_label = Label(master, text = "Mail server port: ")
        self.flag_label = Label(master, text="Replacement flag character: ")
        self.subject_label = Label(master, text="Mail subject: ")
        self.frame_content_label = Label(master, text = "Framework words:")
        self.individual_info_label = Label(master, text = "Ordered information:")



        # vcmd = master.register(self.validate) # we have to wrap the command
        # self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        vcmd2 = master.register(self.validate2)
        self.my_entry = Entry(master, validate = "key", validatecommand = (vcmd2, '%P'))


        # Entry added
        self.account_entry = Entry(master)
        self.pwd_entry = Entry(master)
        self.port_entry = Entry(master)
        self.flag_entry = Entry(master)
        self.subject_entry = Entry(master)



        # self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        # self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        # self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # Button added
        self.upload_button = Button(master, text = "Upload", command = lambda: self.update("upload"))
        self.run_button = Button(master, text = "Run", command = lambda: self.update("run"))

        # Text added
        self.frame_content_text = Text(master, width = 30, height = 20 ,bg = "black" ,fg = "white")
        self.individual_info_text = Text(master, width = 60, height = 20, bg = "black", fg = "white")

        # LAYOUT

        # self.label.grid(row=0, column=0, sticky=W)
        # self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        # self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
        # self.add_button.grid(row=2, column=0)
        # self.subtract_button.grid(row=2, column=1)
        # self.reset_button.grid(row=2, column=2, sticky=W+E)

        # My components layout
        self.account_label.grid(row = 3, column = 0, sticky=W)
        self.account_entry.grid(row = 4, column = 0, columnspan = 8, sticky=W+E)
        self.pwd_label.grid(row = 5, column = 0, sticky=W)
        self.pwd_entry.grid(row = 6, column = 0, columnspan = 8, sticky=W+E)
        self.port_label.grid(row = 7, column = 0, sticky=W)
        self.port_entry.grid(row = 8, column = 0, columnspan = 8, sticky=W+E)
        self.flag_label.grid(row = 9, column = 0, sticky=W)
        self.flag_entry.grid(row = 10, column = 0, columnspan = 8, sticky=W+E)
        self.subject_label.grid(row = 11, column = 0, sticky=W)
        self.subject_entry.grid(row = 12, column = 0, columnspan = 8, sticky=W+E)
        self.upload_button.grid(row = 13, column = 0, sticky = W + E)
        self.run_button.grid(row = 13, column=3, sticky=W + E)
        self.my_label.grid(row = 14, column = 0, columnspan=2, sticky=E)

        self.frame_content_label.grid(row = 15, column = 0, sticky = W)
        self.frame_content_text.grid(row = 16, column = 0, sticky = W)

        self.individual_info_label.grid(row = 15, column = 2, sticky=W)
        self.individual_info_text.grid(row = 16, column = 2, sticky = W)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def validate2(self, new_text):
        if not new_text: # the field is being cleared
            self.my_entry = "Hello, master!"
            return True
        try:
            self.my_text = str(new_text)
            return True
        except ValueError:
            return False

    def transfer(self):
        self.guest.sender = self.account_entry.get()
        self.guest.pwd = self.pwd_entry.get()
        self.guest.flag = self.flag_entry.get()
        self.guest.port_num = self.port_entry.get()
        self.guest.subject = self.subject_entry.get()
        self.guest.host_addr = host_name_match(self.guest.sender)
        self.guest.frame_content = self.frame_content_text.get("1.0", END)
        self.guest.individual_content = self.individual_info_text.get("1.0", END)

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        elif method == "reset":
            self.total = 0
        elif method == "upload":
            self.transfer()
            print self.guest
        else : # run
            print "Running the program"
            self.my_text.set("Send emails automatically!")
            self.guest.run()

        # self.total_label_text.set(self.total)
        # self.entry.delete(0, END)

class Guest(object):

    def __init__(self): # Define basic elements for Guest object
        self.sender = 'cs_architecture@163.com'
        self.pwd = 'password'
        self.receivers = [] # empty set
        self.port_num = 25
        self.host_addr = 'smtp.163.com'
        self.individual_content = ''
        self.flag = 'XX'
        self.frame_content = ''
        self.subject = "Score Result Inform"

    def run(self):
        print("Running process...")
        smtp = smtplib.SMTP()  # Create a smtp instance
        smtp.connect(self.host_addr, self.port_num) # connect to mail server
        smtp.login(self.sender, self.pwd) # Login with a correct account
        multi_send(self, smtp); # call sendemail one after another for different receivers
        smtp.quit() # Unlink the connection and exit
        print("Sending successfully!")

def host_name_match(sender):
    host_name =  'smtp.' + sender.split("@")[1]
    return host_name

def multi_send(guest, smtp):
    # This part should be changed since it's not a txt file anymore
    # fhand = open(guest.individual_txt, 'r');
    # line_set = [] # The Midd for adjustment
    # info_set = [] # The set we will final use
    # all_content = fhand.readlines()
    # for line in all_content:
    #     if (line != '\n'):
    #         line_set.append(line) # delete blank lines from all_content
    # for line in line_set:
    #     ele_set = line.split('\t') # split one line into different elements
    #     ele_set[-1] = ele_set[-1].strip('\n') # Remove the '\n' character
    #     info_set.append(ele_set)   # Fill elements into the set we will use finally
    # #first_line = line_set[1] # This line is colomn name, thus very important (maybe)
    # line_set = []
    # info_set = []

    line_set = guest.individual_content.split('\n')
    info_set = []
    for line in line_set:
        line = line.strip(" ")
        ele_set = line.split('\t')
        if len(ele_set) > 1:
            info_set.append(ele_set)
    print info_set


    # Get all receivers
    for i in range(1, len(info_set)):
        guest.receivers.append(info_set[i][-1]);

    all_specified_content = []
    replacement_flag = guest.flag

    # Get specified content each time
    for i in range(1, len(info_set)):
        # temp_content = guest.content;
        temp_content = guest.frame_content
        for j in range(0, len(info_set[1])-1):
            temp_content = temp_content.replace(replacement_flag, info_set[i][j], 1); # each time replace one flag
        all_specified_content.append(temp_content);


    # Send emails with different contents one by one
    send_seq = 0;
    for single_receiver in guest.receivers:
        msg = MIMEMultipart('mixed')  # Message type, always "mixed"
        msg['Subject'] = guest.subject  # Subject of you email
        msg['From'] = guest.sender          # Sender email info
        msg['To'] = single_receiver    # Receiver email(s) info
        msg['Date'] = str(datetime.date.today())      # Sending Time
        text_plain = MIMEText(all_specified_content[send_seq], 'plain', 'utf-8')  # An necessary transform
        msg.attach(text_plain) # Add text to message lib
        smtp.sendmail(guest.sender, single_receiver, str(msg))
        send_seq += 1;


root = Tk()
my_mailor = Automailor(root)
root.mainloop()  # Use a loop to promise that I can send mails again and again in batch
