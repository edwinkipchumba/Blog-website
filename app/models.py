from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    blogpost = db.relationship('Blogs', backref='author', lazy='dynamic')
    comments = db.relationship('Comments', backref='author', lazy='dynamic')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

#to link tables what you add after backref matters
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'Author: {self.author}'

class Blogs(db.Model):
    __tablename__= 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    topic = db.Column(db.String(255))
    content = db.Column(db.Text)
    date = db.Column(db.DateTime(250), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship('Comments', backref='title', lazy='dynamic')

    def save_blog(self,blogpost):
        db.session.add(blogpost)
        db.session.commit()

    @classmethod
    def get_blogposts(id,title):
        blogpost = Blogs.query.filter_by(title=title).all()
        return blogpost

    def __repr__(self):
        return f"Blogs {self.id}','{self.date}')"

class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime(250), default=datetime.utcnow)
    blogs_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comments = Comments.query.filter_by(blogs_id=id).all()
        return comments

    def __repr__(self):
        return f"Comments('{self.comment}', '{self.date_posted}')"


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    user = db.relationship('User', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)
        

class Subscriber(UserMixin, db.Model):
    __tablename__="subscribers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)


    def save_subscriber(self):
       db.session.add(self)
       db.session.commit()

    @classmethod
    def get_subscribers(cls,id):
       return Subscriber.query.all()


    def __repr__(self):
       return f'User {self.email}'

class Quote:
    """
    Quotes is a  class for quotes  from API given
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote