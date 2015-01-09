from users import UserRepository
from mailer import Mailer
from notifier import Notifier

import unittest
import mock
from mock import call

class NotificationsTestCase(unittest.TestCase):

        def setUp(self):
		self.text="Hello!"

        def test_user_repository(self):
		users=UserRepository()
		user=users.get_user("jaume.moral")
		self.assertEquals("jaume.moral@upc.edu",user['mail'])

	def test_0_user(self):		
		users=mock.create_autospec(UserRepository)
		mailer=mock.create_autospec(Mailer)		
		notifier=Notifier(users,mailer)
		notifier.notify(self.text,[])
		self.assertEqual(mailer.send_mail.call_count,0)

	def test_1_user(self):		
		users=mock.create_autospec(UserRepository)
		users.get_user.return_value={"mail":"jaumem@fib.upc.edu"}
		mailer=mock.create_autospec(Mailer)		
		notifier=Notifier(users,mailer)
		notifier.notify(self.text,["jaume.moral"])
		mailer.send_mail.assert_called_with("jaumem@fib.upc.edu",self.text,self.text)

	def test_2_users(self):
		users=mock.create_autospec(UserRepository)
		users.get_user.side_effect=[{"mail":"jaumem@fib.upc.edu"},{"mail":"anna@fib.upc.edu"}]
		mailer=mock.create_autospec(Mailer)		
		notifier=Notifier(users,mailer)
		notifier.notify(self.text,["jaume.moral","anna.casas"])
                mylist=[
			call("jaumem@fib.upc.edu",self.text,self.text),
			call("anna@fib.upc.edu",self.text,self.text)
 		]
		self.assertEqual(mailer.send_mail.call_args_list,mylist)

if __name__ == '__main__':
	unittest.main()
