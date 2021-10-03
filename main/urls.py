from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index_page'),
    path('about/', about, name='about_page'),
    path('wisher/<int:pk>/', list_page, name='wish_list_page'),

]
