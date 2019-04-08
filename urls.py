from django.urls import path
from django.conf.urls import include, url
from mockingbirds.views import LiveVideoFaceDetect

from . import views
urlpatterns= [path('', views.index, name = "First_view"),
		url(r'^mockingbirds/$', LiveVideoFaceDetect.as_view(), name='live_video'),

       ]