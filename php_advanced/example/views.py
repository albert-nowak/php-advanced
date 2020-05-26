from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from example.forms import GiftListForm
from example.models import GiftList


def hello_world(request):
    return render(request, 'index.html', {})


def hello_name(request, name):
    return HttpResponse(f'Hello, {name}!')


class GiftListListView(ListView):
    model = GiftList
    template_name = 'example/list.html'
    context_object_name = 'gfl_entries'


class PostCreateView(CreateView):
    model = GiftList
    form_class = GiftListForm
    success_url = '/gift_list/add'
    template_name = 'example/add.html'


class PostEditView(UpdateView):
    model = GiftList
    form_class = GiftListForm
    template_name = 'example/add.html'

    @property
    def success_url(self):
        return reverse('list_gfl')
