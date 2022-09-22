from django.urls import path, include

from .views import ThreadsCreate, ThreadsDetail, ThreadsList, comment_create, Developer

urlpatterns = [
    path('threadslist/', ThreadsList.as_view(), name='list'),
    path('detail/<int:pk>/', ThreadsDetail.as_view(), name='detail'),
    path('threads/create/', ThreadsCreate.as_view(), name='tcreate'),
    path('detail/<int:pk>/comments', comment_create, name="ccreate"),
    path('developer/', Developer.as_view(), name='developer'),

]