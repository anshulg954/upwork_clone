# util.py for utility in the website 

import smtplib
from email.mime.text import MIMEText


def mail_function(toaddr, body):
	msg = MIMEText(body,"html")
	subject = "The message of the patient............".title()
	msg['From'] = "mkshsahani852@gmail.com"
	msg['To'] = toaddr
	msg['Subject'] = subject
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("mkshsahani852@gmail.com","Mukesh@9646647402")
	server.send_message(msg)
	# print("send the message........")
	server.quit()


# this is a mail generator for the application
def generate_mail(email_addresss, first_name, des_):
	body = f"""\
			<!doctype html>
			<html>
			<head>
				[{first_name}] ha applied for the jobs.
			</head>
			<body>
				{first_name} has specialization in the {des_}.
				You can contact him  at {email_address}

			</body>
			</html>
			"""
	return body
