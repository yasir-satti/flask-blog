from application import db, login_manager
from flask_login import UserMixin

#create columns in table
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(200), nullable=False, unique=True)
    content = db.Column(db.String(500), nullable=False, unique=True)

    # print result of the operation, helps to see if something gone wrong
    def __repr__(self):
        return ''.join(["User:",self.first_name,self.last_name, "Title:", self.title, "Content: ", self.content])

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))