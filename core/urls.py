from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('shortenUrl', views.createShortenedUrl, name='new_url'),
    path('editUrl/<int:pk>', views.editShortenedUrl, name='edit_url'),
    path('deleteUrl/<int:pk>', views.deleteShortenedUrl, name='delete_url'),

]
