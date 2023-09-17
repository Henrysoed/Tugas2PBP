from django.urls import path
from main.views import show_main
from main.views import show_main, create_item

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
]