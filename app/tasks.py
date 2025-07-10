import rq
from app import create_app, db
from app.email import send_email
from app.models import User, Post, Task
from flask import current_app

def export_posts(user_id):
    app = create_app()
    with app.app_context():
        user = User.query.get(user_id)
        posts = user.posts.order_by(Post.timestamp.asc())
        data = '\n'.join(['%s,%s,%s' % (p.body, p.timestamp, p.author.username) for p in posts])
        send_email('[Microblog] Your posts', sender=current_app.config['ADMINS'][0],
                   recipients=[user.email], text_body=data)
        task = Task.query.get(rq.get_current_job().get_id())
        task.complete = True
        db.session.commit()
