from django.conf.urls import url
from ExpertSystems import views

urlpatterns = [
    url(r'^disease/$', views.disease_list),
    url(r'^disease/(?P<pk>[0-9]+)/$', views.disease_list),
]