from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from core.views import redirectToUrl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('api/', include('core.urls')),
    path('<str:shortened_url>', redirectToUrl, name='redirect_url'),
]
