from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

def default_expiry_time():
    return timezone.now() + timedelta(days=365)

class StoredUrls(models.Model):
    shortened_url = models.CharField(max_length=10, null=True, blank=True)
    redirect_url = models.URLField()
    creation_time = models.DateTimeField(auto_now_add=True, editable=False)
    expiry_time = models.DateTimeField(
        default=default_expiry_time)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Stored URL'
        verbose_name_plural = 'Stored URLs'