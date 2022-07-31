import smtplib 
       
#reply_message = "Your contact have been sent"
server = smtplib.SMTP("smtp.gmail.com", 5000)
server.starttls()
server.login("powerpufffy@gmail.com", "cpjlcidxhdvxeysc")
server.sendmail("powerpufffy@gmail.com", "chojaokun@gmail.com", "hi", "chokun sudlor")

print('sent !')