import smtplib 
import datetime
from email.mime.text import MIMEText
from smtplib import SMTP

originMail = 'chillafterstudy@gmail.com'
pwd = '16kriegergutbose'
destinationMail = ['acvelap@opendeusto.es','uxuegarciaugarte@opendeusto.es','dcasado@opendeusto.es']

msg = MIMEText ("First try sending data")
msg ['Subject'] = 'WARNING'
msg['From'] = originMail
msg['To'] = destinationMail

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(originMail,pwd)
server.sendmail(originMail,destinationMail,msg.as_string())

print("Email sent successfully")

server.quit()
