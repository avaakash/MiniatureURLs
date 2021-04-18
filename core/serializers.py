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
        return obj

    def create(self, validated_data) -> StoredUrls:
        et =  validated_data.get('expiry_time', None)
        if et:
            validated_data['expiry_time'] = timezone.now() + et
        obj = StoredUrls.objects.create(**validated_data)
        obj.shortened_url = idToBase62(obj.pk)
        obj.save()
        return obj

    def update(self, instance: StoredUrls, validated_data) -> StoredUrls:
        et = validated_data.get('expiry_time', None)
        instance.expiry_time = instance.creation_time + et if et else instance.expiry_time
        instance.redirect_url = validated_data.get('redirect_url', instance.redirect_url)
        instance.save()
        return instance

    class Meta:
        model = StoredUrls
        fields = ['shortened_url', 'redirect_url',
                  'expiry_time']


class ShortenedUrlSerializer(serializers.ModelSerializer):
    expiry_time_days = serializers.SerializerMethodField()

    def get_expiry_time_days(self, obj):
        return obj.expiry_time_days()

    class Meta:
        model = StoredUrls
        fields = ['shortened_url', 'redirect_url',
                  'expiry_time', 'creation_time', 'pk', 
                  'expiry_time_days', 'visits']
