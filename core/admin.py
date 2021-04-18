from django.contrib import admin

from .models import StoredUrls


@admin.register(StoredUrls)
class StoredUrlsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'shortened_url',
                    'creation_time', 'expiry_time', 'user']
