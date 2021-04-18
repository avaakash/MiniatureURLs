from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core import views

app_name = 'core'

urlpatterns = [
    path('shortenUrl', csrf_exempt(views.createShortenedUrl), name='new_url'),
    path('allUrls', csrf_exempt(views.getAllUrls), name='get_all_urls'),
    path('editUrl/<int:pk>', csrf_exempt(views.editShortenedUrl), name='edit_url'),
    path('deleteUrl/<int:pk>', csrf_exempt(views.deleteShortenedUrl), name='delete_url'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
