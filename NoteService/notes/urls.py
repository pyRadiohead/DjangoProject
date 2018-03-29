from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    url(r'^$', views.notes_list_view, name='notes_list_view'),
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<note>[-\w]+)/$', views.note_detail_view, name='note_detail_view'),
    path('<int:note_id>/',views.note_detail_view,name ='note_detail_view' )
]