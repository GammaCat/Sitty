from django.db import models


class TASK_STATES:
    in_progress = "P"
    ready = "R"

# Create your models here.


class Task(models.Model):
    TASK_STATES_CHOICES = (
        (TASK_STATES.in_progress, 'in progress'),
        (TASK_STATES.ready, 'ready'),
    )
    title = models.CharField(max_length=200)
    estimate = models.DateField(auto_now=True)
    state = models.CharField(max_length=1, choices=TASK_STATES_CHOICES)

