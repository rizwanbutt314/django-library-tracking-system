import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_system.settings')

app = Celery('library_system')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.CELERYBEAT_SCHEDULE = {
    'check-overdue-loans-daily': {
        'task': 'library.tasks.check_overdue_loans',
        'schedule': crontab(minute=0, hour=16),
        # 'schedule': 20, # run every 20 secs for testing
    },
}