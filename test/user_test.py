#test

u=user(name="example",email="example@gmail.com",password="example")

#adding a user to data base 
u.add()

#authanticateing a user and cheking if he existe or not in the database and return a user object else false 
u.authanticate('ala@gmail.com','5d530613969feac08946e337b5f3b1189b2f0b0ca73a812f4b83a504a0c773b2')

#geting current active user
user_object=u.find_user_by_SessionID('any')
print(user_object)

#loging a user in and seting his session id
print(u.login('mysessionID'))