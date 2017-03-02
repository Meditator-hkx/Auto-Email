# coding: utf-8
# sender = str(raw_input("Sender mail: ")) # raw_input test


import datetime
today = datetime.date.today()
print today

# sender = "hkx@163.com"

# a = [1, 2]
# a.append("hello")
# print a[1],a[-1]
# print 'smtp.' + sender.split("@")[1]

# frame_txt = 'content_framework.txt'
# def get_frame_content(frame_txt):
#     fhand = open(frame_txt, 'r');
#     content = fhand.read();
#     fhand.close();
#     return content
# print get_frame_content(frame_txt)
#
# t = range(2, 4)
# print t
#
#
# individual_txt = 'score_test.txt'
# def multi_send():
#     fhand = open(individual_txt, 'r');
#     line_set = []
#     all_content = fhand.readlines()
#     for line in all_content:
#         if (line != '\n'):
#             line_set.append(line)
#     for line in line_set:
#         ele_set = line.split('\t')
#         ele_set[-1] = ele_set[-1].strip('\n')
#     print len(line_set)
#         # line.strip("\n")
#         # print line
#         # line_ele_set = line.split(" ")
#         # print line_ele_set
#         # for ele in line_ele_set:
#         #     print ele
#         # for ele in line:
#         #     print ele
#
#     # print all_content
#     fhand.close()
#     return 0;

info_content = "Name	Student ID	Course	Score	Email\n  \n \
A	001	CS123	65	a@163.com\n \
B	002	CS124	89	b@qq.com\n  \
C	003	CS125	100	c@hotmail.com"

line_set = info_content.split('\n')
info_set = []
for line in line_set:
    line = line.strip(" ")
    ele_set = line.split('\t')
    if len(ele_set) > 1:
        info_set.append(ele_set)
print info_set
