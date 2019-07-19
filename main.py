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

    id = db.Column(db.Integer, primary_key=True)#how to return this with a title and blog?
    title = db.Column(db.String(120))
    blog = db.Column(db.String(120))
   
    
    def __init__(self, title, blog):
       self.title = title
       self.blog = blog


@app.route('/blog', methods=['POST', 'GET'])
def add_blog():

      if request.method == 'POST':
        
        title = request.form['title']
        blog = request.form['blog'] 
        new_blog_object = Blog(title, blog)
        db.session.add(new_blog_object)
        db.session.commit()
        


        print("this is blogobjectid:   " + str(new_blog_object.id))   

        
      
        
        
        return render_template('addconfirm.html',title=title, blog=blog)



@app.route('/', methods=['POST', 'GET'])
def index():

    
    blogs = db.session.query(Blog).all()
    """
    ids = [blog.id for blog in blogs]
    titles = [blog.title for blog in blogs]
    entries = [blog.blog for blog in blogs]

    test_query = Blog.query.filter_by(id=1).first()
    print("this is testquery:   "  + str(test_query))
    """
    counter = 1
    loop_queries = []
    for objects in blogs:
      loop_query = Blog.query.filter_by(id=counter).first()
      counter += 1
      loop_queries.append(loop_query)
      print("This is loop query"  + str(loop_query))
    
    
    return render_template('blog.html',title="Title for your new blog:", blog="Your blog", loop_queries=loop_queries)
  



if __name__ == '__main__':
    app.run()
