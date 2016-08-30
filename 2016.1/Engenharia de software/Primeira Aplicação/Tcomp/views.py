import jinja2
import os
import webapp2
from datetime import datetime
from google.appengine.ext import db

from models import Notes

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
    jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(
        self,
        filename,
        template_values,
        **template_args
        ):
        template = jinja_environment.get_template(filename)
        self.response.out.write(template.render(template_values))


class MainPage(BaseHandler):

    def get(self):
        self.render_template('index.html', {})

class ShowUsers(BaseHandler):
    
    def get(self):
        notes = Notes.all()
        self.render_template('users_index.html', {'notes': notes})
        

class CreateUser(BaseHandler):
    def post(self):
        n = Notes(author=self.request.get('inputName'),
                  text=self.request.get('inputUsername'),
                  priority=self.request.get('inputPassword'),
                  status=self.request.get('inputPassword'))
        n.put()
        return webapp2.redirect('/showusers')

    def get(self):
        self.render_template('create.html', {})
		
class EditUser(BaseHandler):

    def post(self, note_id):
        iden = int(note_id)
        note = db.get(db.Key.from_path('Notes', iden))
        note.author = self.request.get('inputName')
        note.text = self.request.get('inputUsername')
        note.priority = self.request.get('inputPassword')
        note.date = datetime.now()
        note.put()
        return webapp2.redirect('/showusers')

    def get(self, note_id):
        iden = int(note_id)
        note = db.get(db.Key.from_path('Notes', iden))
        self.render_template('edit.html', {'note': note})
	

class DeleteUser(BaseHandler):

    def get(self, note_id):
        iden = int(note_id)
        note = db.get(db.Key.from_path('Notes', iden))
        db.delete(note)
        return webapp2.redirect('/showusers')


class Login(BaseHandler):

    def post(self):
        validation = "false"
        username = self.request.get('inputUsername')
        password = self.request.get('inputPassword')
        notes = Notes.all()
        for note in notes:
            if note.text == username:
                if note.priority == password:
                    return webapp2.redirect('/first/'+note.text)
        return webapp2.redirect('/login')

    def get(self):
        self.render_template('login.html', {})

class First(BaseHandler):

    def post(self, id):
        first_number = self.request.get('numberOne')
        second_number = self.request.get('numberTwo')
        res = (int(second_number)) / (int(first_number))
        return webapp2.redirect('/second/'+str(res))

    def get(self, id):
        username = id
        notes = Notes.all()
        for note in notes:
            if note.text == username:
                self.render_template('first.html', {'note': note})
		
class Second(BaseHandler):

    def get(self, id):
        sum = id
        self.render_template('second.html', {'sum': sum})
