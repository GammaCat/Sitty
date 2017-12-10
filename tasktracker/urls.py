
from django.conf.urls import url

from tasktracker.views import tasks
from tasktracker.views import roadmaps

urlpatterns = [
    url(r'^tasks/$', tasks),
    url(r'^road-maps/$', roadmaps),
]
