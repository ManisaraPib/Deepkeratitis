


# import smtplib, ssl
# import socket

# port = 465  # For SSL
# smtp_server = 'localhost'
# sender_email = "powerpufffy@gmail.com"  # Enter your address
# receiver_email = "chojaokun@gmail.com"  # Enter receiver address
# password = input("cpjlcidxhdvxeysc")
# message = """\

# Subject: Hi there

# This message is sent from Python."""

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

# print('sent !')




import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = """Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
"""
#The mail addresses and password
sender_address = 'powerpufffy@gmail.com'
sender_pass = 'cpjlcidxhdvxeysc'
receiver_address = "chojaokun@gmail.com"
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')