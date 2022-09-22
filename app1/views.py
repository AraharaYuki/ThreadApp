from concurrent.futures import thread
from turtle import title
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from app1.models import Thread, Comment

class ThreadsList(ListView):
    template_name = 'list.html'
    model = Thread


class ThreadsDetail(DetailView):
    template_name = 'detail.html'
    model = Thread
    fields = ('content',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(thread=self.kwargs['pk'])
        return context

class ThreadsCreate(CreateView):
    template_name = 'threadscreate.html'
    model = Thread
    fields = ('title',)
    success_url = reverse_lazy('list')


def comment_create(request, pk):
    Comment.objects.create(content=request.POST['content'],
    thread_id=pk)
    url = f'/detail/{pk}/'
    return redirect(to=url)


class Developer(ListView):
    template_name: str = "developer.html"
    model = Thread
