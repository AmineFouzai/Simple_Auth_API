
'''
Preset controller by torn for / route
'''
from .modules import *

class Base_Handler(tornado.web.RequestHandler):
		def get_current_user(self):
			  return self.get_secure_cookie('SessionID')

class HomeHandler(Base_Handler):
	
	@tornado.web.authenticated
	def get(self):
		curent_SessionID=tornado.escape.xhtml_escape(self.get_current_user())
		client=user()
		self.write(tornado.escape.json_encode(tornado.escape.json_decode(client.find_user_by_SessionID(curent_SessionID))))
	
class SignUP_Request_Handler(Base_Handler):
		

	def post(self):
			
		SessionID=uuid4()
		self.set_secure_cookie('SessionID',str(SessionID))
		client=user(self.get_argument('name'),self.get_argument('email'),self.get_argument('password'),str(SessionID))
		if not client.add_user():
			self.redirect(url='/signup',permanent=False,status=302)  
		else:
			client.add_user()
			self.redirect(url='/',permanent=True,status=301)
	

class Login_Request_Handler(Base_Handler):

	def post(self):
		SessionID=uuid4()
		self.set_secure_cookie('SessionID',str(SessionID))
		client=user(email=self.get_argument('email'),password=self.get_argument('password'))
		if client.login(str(SessionID)): 
			self.redirect(url='/',permanent=True,status=301)
		else:
			self.redirect(url='/login',permanent=False,status=302)

class Logout_Request_Handler(Base_Handler):
	def get(self):
		self.clear_all_cookies()
		self.redirect('/login')

