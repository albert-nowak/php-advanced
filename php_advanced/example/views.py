from django.http import HttpResponse
from django.shortcuts import render

from example.models import GiftList


def hello_world(request):
    return render(request, 'index.html', {})


def hello_name(request, name):
    return HttpResponse(f'Hello, {name}!')


def simple_list_view(request):
    gfl_entries = GiftList.objects.all()
    return render(
        request,
        'example/list.html',
        {'gfl_entries': gfl_entries}
    )
