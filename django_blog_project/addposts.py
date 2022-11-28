import json
from blog.models import Post
with open('posts.json') as f:
    posts = json.load(f)
for post in posts:
    post=Post(title=post['title'],content=post['content'],author_id=post['user_id'])
    post.save()