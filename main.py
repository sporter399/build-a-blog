from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['DEBUG'] = True
project_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{}".format(os.path.join(project_dir, "build-a-blog.db"))
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    blog = db.Column(db.String(120))
   
    
    def __init__(self, title, blog):
       self.title = title
       self.blog = blog

    def __repr__(self):
        return ('%r' % self.title, '%r' % self.blog)
        
       

methods=['POST', 'GET']
def add_title():
     
     if request.method == 'POST':
        print("do i execute")
        title = request.form['title']
        new_title = Blog(title)
        
        db.session.add(new_title)
        db.session.commit()

        
        titles = Blog.query.all()
        return render_template('addconfirm.html',title=title)

@app.route('/blog', methods=['POST', 'GET'])
def add_blog():

     if request.method == 'POST':
        print("print here")
        blog = request.form['blog']
        print(blog)
        new_blog = Blog(blog)
        db.session.add(new_blog)
        db.session.commit()

        
        blogs = Blog.query.all()
        return render_template('addconfirm.html',title=title, blog=blog)



@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('blog.html',title="Title for your new blog:", blog="Your blog")
  



if __name__ == '__main__':
    app.run()
