class UserRepository:
	def get_user(self,username):
		return {"username:":username,"mail":username+"@upc.edu"}
