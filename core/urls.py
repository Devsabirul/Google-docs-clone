from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="home"),
    path('edit-file/<int:id>', editfile, name="editfile"),
]
