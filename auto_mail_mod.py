# coding: utf-8
# author: Meditator_hkx
# Test passed with simple information

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

sender = 'cs_architecture@163.com' # sender mail info, should be real
receiver = ['a@163.com', 'b@qq.com', 'c@sjtu.edu.cn'] # Receiver mail info set, should be real


#### Basic Configure Information ####
user_name = sender # sender account name, should be correct
pwd = 'password' # Password corresponding to the sender account name, should be correct
host_addr = 'smtp.163.com' # The mail server host name, for QQ, it should be 'smtp.qq.com' , when you use different mail servers, please offer corresponding host names
port_num = 25 # Server port, it should be 465 for QQ, when you use different mail servers, please offer corresponding server ports
############################

#### Email Header Information ####
msg = MIMEMultipart('mixed')  # Message type, always "mixed"

subject = 'Auto email test!'
msg['Subject'] = subject      # Subject of you email

msg['From'] = sender          # Sender email info
msg['To'] = ";".join(receiver)# Receiver email(s) info
msg['Date']='2999-12-31'       # Sending Time
############################

#### Main Body ####
# In this part you can write any information for your own need.
course = 'Computer Language'
score = 90 # Test number of exam result
text = "Hi!\nHow are you?\nHere is your score of course  " + course + " this term: " + str(score)
text_plain = MIMEText(text,'plain', 'utf-8') # An necessary transform
msg.attach(text_plain) # Add text to message lib
############################

#### Standard process ####
smtp = smtplib.SMTP()  # Create a smtp instance
smtp.connect(host_addr, port_num) # connect to mail server
smtp.login(user_name, pwd) # Login with a correct account
smtp.sendmail(sender, receiver, str(msg)) # send mail
smtp.quit() # Unlink the connection and exit
