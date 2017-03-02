#coding: utf-8
# Test pass

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header

sender = 'cs_architecture@163.com'
receiver = ['a@163.com', 'b@qq.com']
num = 90

user_name = 'cs_architecture@163.com'
pwd = 'password'
host_addr = 'smtp.163.com'
port_num = 25

subject = 'Auto email test!' # email subject
msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = '<cs_architecture@163.com>'
msg['To'] = ";".join(receiver)
msg['Date']='2012-3-16'


text = "Hi!\nHow are you?\nHere is the score you wanted:\n" + str(num)
text_plain = MIMEText(text,'plain', 'utf-8')
msg.attach(text_plain)




 smtp = smtplib.SMTP()
 smtp.connect(host_addr, port_num)
 smtp.login(user_name, pwd)

 smtp.sendmail(sender, receiver, str(msg))
 smtp.quit()
