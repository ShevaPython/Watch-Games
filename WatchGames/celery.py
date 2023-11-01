import os
from celery import Celery

# задать стандартный модуль настроек Django
# для программы 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WatchGames.settings')
app = Celery('WatchGames')
app.config_from_object('django.conf:settings', namespace='CELERY')
print("Broker URL:", app.conf.broker_url)
