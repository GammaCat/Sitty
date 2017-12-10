from django.shortcuts import render

from .models import Task
from .models import RoadMap

# Create your views here.


def tasks(request):

    task_list = list(Task.objects.all())

    return render(
        request,
        'tasks.html',
        {'task_list': task_list}
    )


def roadmaps(request):

    roadmaps_list = list(RoadMap.objects.all())

    return render(
        request,
        'roadmaps.html',
        {
            'roadmaps_list': roadmaps_list
        }
    )
