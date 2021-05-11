import os
import smtplib
import imghdr
from email.message import EmailMessage

mail_list = ["jawadsgs3@gmail.com",
             "imjawadhossain@gmail.com",
             "brycetonkin1@gmail.com",
             "itsjessicaloera@gmail.com"
             ]

E_A = os.environ.get('ine')
E_P = os.environ.get('password')
msg = EmailMessage()
msg['Subject'] = "This final test"
msg['From'] = E_A
msg['Bcc'] = mail_list
msg.set_content("would you like this Image?",E_A, E_P)

with open('GroupEvents.jpg', 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(E_A, E_P)
    smtp.send_message(msg)

