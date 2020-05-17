from pymongo import MongoClient
from  tornado.escape import json_decode
from bson.json_util import dumps
import hashlib



class user(object):
    def __init__(self,name=None,email=None,password=None,SessionID=None):
        client=MongoClient('localhost', 27017)
        self.db=client.user
        self.name=name
        self.email=email
        self.password=hashlib.sha256(str(password).encode('UTF-8')).hexdigest()
        self.SessionID=SessionID
        
    def add_user(self):
    
        return self.db.users.insert_one({
            "name":self.name,
            "email":self.email,
            "password":self.password,
            'SessionID':self.SessionID
        }) if not self.authanticate(email=self.email,password=self.password) else False
        
    def find_user_by_SessionID(self,SessionID):
        document=self.db.users.find_one({'SessionID':SessionID})
        return dumps(document)


    def authanticate(self,email,password):
        user=dict()
        document=self.db.users.find_one({'email':email,'password':password})
        return True if document else False

    def login(self,SessionID):
        if self.authanticate(email=self.email,password=self.password):
            self.db.users.find_one_and_update({'email':self.email,'password':self.password},{"$set":{"SessionID":str(SessionID)}})
            return True
        else:
            return False

        
