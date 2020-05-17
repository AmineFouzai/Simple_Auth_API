
'''
Middleware for controller to contain all the modules
'''
import tornado.web
import tornado.escape
from uuid import uuid4
from models.user import user	
import hashlib        