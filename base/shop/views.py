from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . import models


def index(request):
    courses = models.Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'shop/courses.html', context=context)

def single_course(request, id):
    # Exemple 1
    # try:
    #     course = models.Course.objects.get(pk=id)
    #     context = {
    #         'course': course
    #     }
    #     return render(request, 'shop/single_course.html', context=context)
    # except models.Course.DoesNotExist:
    #     raise Http404()

    # Exemple 1
    course = get_object_or_404(models.Course, pk=id)
    context = {
        'course': course
    }
    return render(request, 'shop/single_course.html', context=context)