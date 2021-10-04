from django.urls import path
from main.views import index, about, list_page

urlpatterns = [
    path('', index, name='index_page'),
    path('about/', about, name='about_page'),
    path('wish-list/<int:pk>/', list_page, name='wish_list_page'),

]
