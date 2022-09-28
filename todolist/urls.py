from django.urls import path
from todolist.views import show_html
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_task

# TODO: Implement Routings Here

app_name = "todolist"

urlpatterns = [
    path('', show_html, name = "show_html"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='create-task'),
]