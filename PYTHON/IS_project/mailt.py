import smtplib


user = "srinivaskulal79@gmail.com"
private_key = "1234"

server = smtplib.SMTP('smtp.gmail.com' , 587)

server.starttls()
print("starting server")
#enable 2fa in senders account create a new apppassword
#here is the receivers mail
#password for senders requires you to create a apppassword
#https://www.youtube.com/watch?v=weA4yBSUMXs
#link to create app password
server.login('isprojectmit2024@gmail.com' , 'cbyn eoro gief jtof')
print("login")
#here is the senders mail
server.sendmail('isprojectmit2024@gmail.com' , user , private_key)

print("Mail sent")


