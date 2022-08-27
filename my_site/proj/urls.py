from urllib import request
from django.urls import path, re_path 
from . import views

urlpatterns = [
    path('', views.DocumentListView.as_view(), name='project'),
    #path('', views.index, name='project'),
    path('load/', views.model_form_upload, name='load'),
    re_path(r'^(?P<pk>\d+)/$', views.DocumentDetailView.as_view(), name="post_single"),
]
