from app.core.celery.app import celery_app

@celery_app.task
def print_message():
    print('message_from_periodic')


celery_app.conf.beat_schedule = {
    'run-every-10-seconds': {
        'task': 'tasks.print_message',
        'schedule': 10.0,  # Запускать каждые 10 секунд
    },
}
