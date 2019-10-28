from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('POST/', views.post_create),
    path('<int:id>/DELETE/', views.post_delete),
    path('LIST/', views.post_list, name= 'list'),
    path('<int:id>/edit/', views.post_update, name='Update'),
   # path('GET/(?P<id>\d+)/', views.post_get),
    path('GET/<int:id>/', views.post_get,name= 'Detail'),
]