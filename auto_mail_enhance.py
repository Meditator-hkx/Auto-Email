# coding: utf-8
# author: Meditator_hkx
# 2017-3-1
# Add information extraction and analyzation ability
# OOP Design

import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header


def host_name_match(sender):
    host_name =  'smtp.' + sender.split("@")[1]
    print host_name
    return host_name

def get_frame_content(frame_txt):
    fhand = open(frame_txt, 'r');
    content = fhand.read();
    return content

def multi_send(guest, smtp):
    fhand = open(guest.individual_txt, 'r');
    line_set = [] # The Midd for adjustment
    info_set = [] # The set we will final use
    all_content = fhand.readlines()
    for line in all_content:
        if (line != '\n'):
            line_set.append(line) # delete blank lines from all_content
    for line in line_set:
        ele_set = line.split('\t') # split one line into different elements
        ele_set[-1] = ele_set[-1].strip('\n') # Remove the '\n' character
        info_set.append(ele_set)   # Fill elements into the set we will use finally
    #first_line = line_set[1] # This line is colomn name, thus very important (maybe)

    # Get all receivers
    for i in range(1, len(info_set)):
        guest.receivers.append(info_set[i][-1]);


    all_specified_content = []
    replacement_flag = guest.flag

    # Get specified content each time
    for i in range(1, len(info_set)):
        # temp_content = guest.content;
        temp_content = get_frame_content(guest.framework_txt);
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



class Guest(object):

    def __init__(self): # Define basic elements for Guest object
        self.sender = 'cs_architecture@163.com'
        self.pwd = 'password'
        self.receivers = [] # empty set
        self.port_num = 25
        self.host_addr = 'smtp.163.com'
        self.framework_txt = 'content_framework.txt'
        self.individual_txt = 'score_test.txt'
        self.flag = 'XX'
        self.frame_content = []
        self.subject = "Score Result Inform"

    def getGuestInfo(self): # Interact with user
        self.sender = str(raw_input("Please input sender email: "))
       # self.host_addr = str(raw_input("Please input server host name: "))
        self.host_addr = host_name_match(self.sender)
        self.port_num = int(raw_input("Please input server port number: "))
        self.framework_txt = str(raw_input("The framework txt file name \
        (should be included in the same directory) is: "))
        self.individual_txt = str(raw_input("The information for replacement is stored\
         in txt (format should follow our rules,\
         which you should refer to score_info.txt) whose file name is: "))
        self.frame_content = get_frame_content(self.framework_txt)
        self.flag = str(raw_input("The special flag character in your framework is: "))
        self.subject = str(raw_input("The subject of your mail is: "))

    def run(self):
        print("Running process...")
        smtp = smtplib.SMTP()  # Create a smtp instance
        smtp.connect(self.host_addr, self.port_num) # connect to mail server
        smtp.login(self.sender, self.pwd) # Login with a correct account
        multi_send(self, smtp); # call sendemail one after another for different receivers
        smtp.quit() # Unlink the connection and exit
        print("Sending successfully!")


#### Run the program ####
g = Guest();
# g.getGuestInfo(); # In test process it's not used
g.run()


