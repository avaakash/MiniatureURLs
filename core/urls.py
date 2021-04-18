from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from core import views

app_name = 'core'

urlpatterns = [
    path('shortenUrl', csrf_exempt(views.createShortenedUrl), name='new_url'),
    path('editUrl/<int:pk>', csrf_exempt(views.editShortenedUrl), name='edit_url'),
    path('deleteUrl/<int:pk>', csrf_exempt(views.deleteShortenedUrl), name='delete_url'),

]
