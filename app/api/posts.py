@bp.route('/posts/', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.paginate(page, current_app.config['POSTS_PER_PAGE'], False)
    data = {
        'items': [p.to_dict() for p in posts.items],
        'total': posts.total,
        'pages': posts.pages,
        'next': url_for('api.get_posts', page=page+1) if posts.has_next else None,
        'prev': url_for('api.get_posts', page=page-1) if posts.has_prev else None
    }
    return jsonify(data)