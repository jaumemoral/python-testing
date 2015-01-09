from users import UserRepository
from mailer import Mailer
import sys

class Notifier:
	def __init__(self,user_repository=UserRepository(),mailer=Mailer()):
		self.user_repository=user_repository
		self.mailer=mailer

	def notify(self,message,usernames):
		for username in usernames:
			user=self.user_repository.get_user(username)
			mail=user['mail']
			self.mailer.send_mail(mail,message,message)

if __name__ == "__main__":
	notifier=Notifier()
	notifier.notify (sys.argv[1],sys.argv[1:])
