
from controllers import *
from tornado.web import url
route = [
		url(
			r"/",
			home.HomeHandler
		),
		url(
			r'/signup',
			home.SignUP_Request_Handler
		),
		url(
			r"/login",
			home.Login_Request_Handler
		),
		url(
			r'/logout',
			home.Logout_Request_Handler
		)
]
					