import webapp2
from views import MainPage, ShowUsers, CreateUser, DeleteUser, EditUser, Login, First, Second

app = webapp2.WSGIApplication([
        ('/', MainPage), 
        ('/showusers', ShowUsers), 
        ('/create', CreateUser), 
        ('/edit/([\d]+)', EditUser),
        ('/delete/([\d]+)', DeleteUser),
        ('/login', Login), 
        ('/first/([\w]+)', First), 
        ('/second/([\d]+)', Second), 
        ],
        debug=True)
