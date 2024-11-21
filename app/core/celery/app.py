import celery  # type: ignore

includes_celery = ['app.core.celery.tasks']
celery_app = celery.Celery(
    'tasks',
    broker='redis://redis:6379/1',
    backend='redis://redis:6379/1',
    include=includes_celery
)
