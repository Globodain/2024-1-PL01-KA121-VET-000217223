from rq import get_current_job # type: ignore
from app import db
from app.models import Task # type: ignore
from flask import current_app

def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()
        
        task = db.session.get(Task, job.get_id())
        if task:
            task.user.add_notification('task_progress', {
                'task_id': job.get_id(),
                'progress': progress
            })
            if progress >= 100:
                task.complete = True
            db.session.commit()

  