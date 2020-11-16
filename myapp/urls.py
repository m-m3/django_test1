from django.urls import path

from myapp.views import list_view, create_view, update_view, delete_view

urlpatters = [
    path('list/view/', list_view, name='list_view'),
    path('create/view/', create_view, name='create_view'),
    path('update/view/', update_view, name='update_view'),
    path('delete/view/', delete_view, name='delete_view'),
]
