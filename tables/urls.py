from django.urls import path
from tables.views import home
urlpatterns = [path('', home),]