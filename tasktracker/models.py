from django.db import models

from datetime import date as dt


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
    estimate = models.DateField()
    state = models.CharField(max_length=1, choices=TASK_STATES_CHOICES)

    def ready(self):
        self.state = TASK_STATES.ready

    def is_failed(self):

        return True if self.state == TASK_STATES.in_progress and self.estimate < dt.today() else False

    def remaining(self):

        return self.estimate - dt.today() if self.state == TASK_STATES.in_progress else 0


