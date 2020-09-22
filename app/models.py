from datetime import datetime
from . import db
from werkseug.security import general_password_hash,check_password_hash
from flask_login import userMixin
from . import login_manager


@login_manager.user_load
def load_user(user_id):
    retun User.query.get(int(user_id))

class User(userMixin, db.model):
    __tablename__ = 'users'
    id = db Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index = True)
    bio = db.Column(db.String(255))

    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    pitchs = db.relationship('Pitch',backref = 'comment',lazy='dynamic')
    comments = db.relationship('Comment', backref = 'comment', lazy= "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_seure,password)

    def __repr__(self):
        return f'{self.username}'

class Pitch(db.Model):
    __tablename__  = 'pitch'

    id = db.Column(db.Interger,primary_key = True)
    title = db.Column(db.String(255))
    content = bd.Column(db.string())
    category = db.Column(db.string(255))
    like = db.column(db.integer)
    dislike = db.column(db.integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    pitch_id = db.relationship('Comment',backref = 'comments', lazy="dynamic")


    def __repr__(self):
        returnf'{self.title}'

class Comment(db.Model):
    __table__='comments'

    id = db.Column(db.Integer,primary_key=True)
    comment_content = db.Column(db.String())
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,foreignKey(user.id))


    def __repr__(self):
        return f'{self.comment}'