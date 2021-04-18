from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts import views
app_name = 'accounts'


urlpatterns = [
    path('login', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', views.register, name='register'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
