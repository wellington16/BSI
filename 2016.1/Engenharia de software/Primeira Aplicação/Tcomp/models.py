from google.appengine.ext import db


class Notes(db.Model):

    author = db.StringProperty()
    text = db.StringProperty()
    priority = db.StringProperty()
    status = db.StringProperty()
    date = db.DateTimeProperty(auto_now_add=True)
