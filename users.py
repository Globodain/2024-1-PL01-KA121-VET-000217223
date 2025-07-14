from app.models import User # type: ignore

@bp.route('/users/<int:id>', methods=['GET']) # type: ignore
def get_user(id):
    return db.get_or_404(User, id).to_dict() 