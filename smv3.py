from email.message import EmailMessage
import smtplib

FROM = "chillafterstudy@gmail.com"
TO = "uxuegarciaugarte@opendeusto.es"
message = "¡Hola, mundo!"

email = EmailMessage()
email["From"] = FROM
email["To"] = TO
email["Subject"] = "Correo de prueba"
email.set_content(message)

smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(FROM, "cdfhgkfaomjmpblr")
smtp.sendmail(FROM, TO, email.as_string())
smtp.quit()