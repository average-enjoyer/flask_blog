from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

posts_list = []

@app.route('/')
def home():
    blogs_url = "https://api.npoint.io/c790b4d5cab58020d391"
    posts = requests.get(blogs_url).json()
    posts_list.clear()
    for post in posts:
        posts_list.append(Post(id=post["id"], title=post["title"], subtitle=post["subtitle"], body=post["body"]))
    return render_template("index.html", posts=posts_list)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return render_template("post.html", posts=posts_list, id=post_id)

if __name__ == "__main__":
    app.run(debug=True)
