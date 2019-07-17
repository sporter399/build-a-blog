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
    name = db.Column(db.String(120))
    titles = db.relationship('Title')
    name = db.Column(db.String(120))
    blogs = db.relationship('Blog')
    
    def __init__(self):
        self.name = name
       

@app.route('/blog', methods=['POST', 'GET'])
def add_title():

     if request.method == 'POST':
        title = request.form['title']
        print('title here')
        new_title = Blog(title)
        db.session.add(new_title)
        db.session.commit()
        
        return render_template('blog.html',title="Title for your new blog:")
"""
@app.route('/blogdisplay', methods=['POST', 'GET'])
def blog_display():


    # all this page does is display

    
    return redirect('/')
"""

@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('blog.html',title="Title for your new blog:")
  



if __name__ == '__main__':
    app.run()
