from django.shortcuts import render

from .models import Task

# Create your views here.


def tasks(request):

    task_list = list(Task.objects.all())

    return render(
        request,
        'tasks.html',
        {'task_list': task_list}
    )
