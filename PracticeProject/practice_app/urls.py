from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^post/', views.post_question, name='post_question'),
    url(r'^home/', views.go_home, name='go_home'),
    url(r'^list/$', views.list_questions, name='list'),
    url(r'^list/(?P<pk>[0-9]+)/$', views.view_question, name='view_question'),
    url(r'^list/delete/(?P<pk>[0-9]+)/$', views.delete_question, name='delete_question'),
    url(r'^list/edit/(?P<pk>[0-9]+)/$', views.edit_question, name='edit_question'),
]
