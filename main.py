from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3

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



@app.route('/test', methods=['POST', 'GET'])
def test():
     
      return render_template('blogenter.html',title="Title for your new blog:", blog="Your blog")       

@app.route('/addconfirm', methods=['POST', 'GET'])
def addconfirm():
      
      if request.method == 'POST':
       
        title = request.form['title']
        blog = request.form['blog'] 
        new_blog_object = Blog(title, blog)
        db.session.add(new_blog_object)      
        db.session.commit()

      return render_template('addconfirm.html', title=title, blog=blog)       

@app.route('/display/<int:post_id>', methods=['POST', 'GET'])#this still doesn't look that good right now
def display(post_id):

      display_list = []

      displayed_blog_object = Blog.query.filter_by(id=post_id).first()
      display_list.append(displayed_blog_object)
     
      return render_template('blogdisplay.html', display_list=display_list)


@app.route('/', methods=['POST', 'GET'])
def index():

    blogs = db.session.query(Blog).all()
    
    counter = 1
    loop_queries = []
    for objects in blogs:
      loop_query = Blog.query.filter_by(id=counter).first()
      counter += 1
      loop_queries.append(loop_query)
    
    
    return render_template('blog.html',loop_queries=loop_queries)
  



if __name__ == '__main__':
    app.run()
