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
"""
    def __repr__(self):
        return ('%r' % self.title, '%r' % self.blog)
"""
        

@app.route('/blog', methods=['POST', 'GET'])
def add_blog():

      if request.method == 'POST':
        
        title = request.form['title']
        blog = request.form['blog'] 
        new_blog_object = Blog(title, blog)
        db.session.add(new_blog_object)
        db.session.commit()
      
        
        
        return render_template('addconfirm.html',title=title, blog=blog)



@app.route('/', methods=['POST', 'GET'])
def index():

    """
    note to self: below is the html code i found online which i thought was commented out in html:
    <li><a href="/{{kitchen_location[0]}}/">{{kitchen_location[0]}}</a></li>
    """
    
    blogs = db.session.query(Blog).all()

    titles = [blog.title for blog in blogs]

    print(titles)
    
    return render_template('blog.html',title="Title for your new blog:", blog="Your blog", titles=titles)
  



if __name__ == '__main__':
    app.run()
