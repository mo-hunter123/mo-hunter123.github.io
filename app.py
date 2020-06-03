from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)

#where data base gonna be stored
#link to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Blogposts.db'

#link app to database
db = SQLAlchemy(app)

#creating table for a post
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)
    author = db.Column(db.String(20), nullable = False, default = 'Anonymous')
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)

    def __repr__(self):
        return "Blog with id = " + str(self.id)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/postcreator')
def test():
    return render_template("postCreator.html")

@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'POST': 
        #we will add data coming from form to database red it than send it
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title = post_title, content = post_content, author = post_author)

        #add the new post to the db
        db.session.add(new_post)
        db.session.commit()

        return redirect('/posts')

    else:    
        all_posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
        return render_template("posts.html", postss = all_posts)


#add updating and deleting and filtering posts 

if __name__ == "__main__":
    app.run(debug=True)