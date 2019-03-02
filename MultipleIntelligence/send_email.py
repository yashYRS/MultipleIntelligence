import smtplib
from email.mime.multipart import MIMEMultipart  #MIME stands for Multipurpose Internet Mail Extension
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import credentials as CD 

def get_text(curr_score) : 
	body = """Respected Sir/Madam, 

As part of a new initiative, the Ministry of Culture, Government of India has released a game, during the run of which 
several aspects of the player's intelligence is evaluated. Your ward registered on our website, and played the game, 
and a detailed report of the performance is attached to this email.

Based on the report, we suggest the following professional options that you could encourage your ward to go through.

"""
	#body = body + get_professions(curr_score) 
	end_body = """

Regards, 
Ministry of Culture
"""

	body = body + end_body 
	return body 







def get_credentials() : 
	### --- decide sender , password , receiver 
	sender = CD.sender
	password = CD.password 
	receiver = CD.receiver

	return sender , password , receiver 


def send_report(file_path) : 

	file = open(file_path, 'rb')
	sender , password , receiver = get_credentials() 

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(sender, password)

	message = MIMEMultipart()
	message['From'] = sender
	message['To'] = receiver
	message['Subject'] = ' Detailed report for your childs session at ** sitename here ** (hosted by Ministry of Culture) '

	body = get_text(1)
	message.attach(MIMEText(body, 'plain'))

#Attachment
	msgObj = MIMEBase('application', 'octet-stream')
	msgObj.set_payload(file.read())
	encoders.encode_base64(msgObj)
	msgObj.add_header('Content-Disposition', 'attachment' ,filename = file_path )
	message.attach(msgObj)

	text = message.as_string()
	server.sendmail(sender, receiver, text)
	server.quit()
