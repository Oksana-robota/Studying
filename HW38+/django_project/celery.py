import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '.settings')

app = Celery('django_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'user_time_print': {
        'task': 'user.tasks.all_users_list',
        'schedule': 60,
        'args': (),
        'kwargs': {},
    }
}