import os
import smtplib
import imghdr
from email.message import EmailMessage

mail_list = ["jawadsgs3@gmail.com",
             "imjawadhossain@gmail.com"
             ]

E_A = os.environ.get('ine')
E_P = os.environ.get('password')
msg = EmailMessage()
msg['Subject'] = "8:0140 Time"
msg['From'] = "Jessica<"+E_A+"ppaayeel@gmail.com>"
msg['Bcc'] = mail_list
msg.set_content("would you like this Image?")

# # This code for Attachat Image file.
# #########################################################################################################
# files = ['GroupEvents.jpg', 'GroupEvents1.jpg']
# for file in files:
#
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name
#
#     msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
# ##########################################################################################################
#
#
# # This code for attuchate Pdf file.
# ##########################################################################################################
# files1 = ['MarkSeet1.pdf', 'MarkSeet.pdf']
# for file1 in files1:
#
#     with open(file1, 'rb') as f1:
#         file_data1 = f1.read()
#         file_name1 = f1.name
#
#     msg.add_attachment(file_data1, maintype='application', subtype='octet-stream', filename=file_name1)
# ##########################################################################################################

#msg.add_alternative(Massage.html, subtype='html')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(E_A, E_P)
    smtp.send_message(msg)

