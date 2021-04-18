from rest_framework import serializers

from django.utils import timezone
from datetime import timedelta

from core.models import StoredUrls
from core.utils import idToBase62


class CreateShortenedUrlSerializer(serializers.ModelSerializer):
    expiry_time = serializers.IntegerField(required=False)

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        et = validated_data.get('expiry_time', None)
        print(et)
        if et:
            validated_data['expiry_time'] = timedelta(days=et)
            print(validated_data['expiry_time'])
        return validated_data
    
    def save(self, **kwargs):
        obj = super().save(**kwargs)
    #     if not obj.shortened_url:
    #         obj.shortened_url = idToBase62(obj.pk)
    #         obj.save()
        return obj

    def create(self, validated_data) -> StoredUrls:
        et = validated_data.get('expiry_time', None)
        print(et)
        if et:
            validated_data['expiry_time'] = timezone.now() + timedelta(days=et)
            print(validated_data['expiry_time'])
        obj = StoredUrls.objects.create(**validated_data)
        obj.shortened_url = idToBase62(obj.pk)
        obj.save()
        return obj
    
    def update(self, instance: StoredUrls, validated_data) -> StoredUrls:
        et = validated_data.get('expiry_time',None)
        instance.expiry_time = instance.creation_time + et if et else instance.expiry_time
        instance.save()
        return instance

    class Meta:
        model = StoredUrls
        fields = ['shortened_url', 'redirect_url',
                  'expiry_time']


class ShortenedUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoredUrls
        fields = ['shortened_url', 'redirect_url',
                  'expiry_time']