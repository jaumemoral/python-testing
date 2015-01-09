import smtplib
from email.mime.text import MIMEText

sender="reply@fib.upc.edu"

class Mailer:
	def send_mail(self,mail,subject,body):
		msg = MIMEText(body)
		msg['Subject'] = subject
		msg['From'] = sender
		msg['To'] = mail

		s = smtplib.SMTP('localhost')
		s.sendmail(sender, [mail], msg.as_string())
		s.quit()
