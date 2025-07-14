from flask import redirect, url_for, flash
from flask_login import login_required, current_user # type: ignore
from app import db
from flask_babel import _ # type: ignore

@bp.route('/export_posts') # type: ignore
@login_required
def export_posts():
    if current_user.get_task_in_progress('export_posts'):
        flash(_('An export task is currently in progress'))
    else:
        current_user.launch_task('export_posts', _('Exporting posts...'))
        db.session.commit()
    return redirect(url_for('main.user', username=current_user.username))


