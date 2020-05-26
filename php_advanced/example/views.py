from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from example.models import GiftList


def hello_world(request):
    return render(request, 'index.html', {})


def hello_name(request, name):
    return HttpResponse(f'Hello, {name}!')


class GiftListListView(ListView):
    model = GiftList
    template_name = 'example/list.html'
    context_object_name = 'gfl_entries'
