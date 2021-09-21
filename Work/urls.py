from django.urls import path , include
from . import views

urlpatterns = [
    path('' , views.index) ,
    path('events/<slugID>' , views.about) ,
    path('comp/<slugID>' , views.comp)
]
