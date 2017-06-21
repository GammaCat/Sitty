
from django.conf.urls import url

from tasktracker.views import tasks

urlpatterns = [
    url(r'^tasks/$', tasks),
]
