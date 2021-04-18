from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponsePermanentRedirect, Http404, HttpResponseServerError
from django.http.response import HttpResponse
from django.utils import timezone

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from core.serializers import ShortenedUrlSerializer, CreateShortenedUrlSerializer
from core.models import StoredUrls
from core.response import StandardResponseStructure


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createShortenedUrl(request) -> Response:
    r = StandardResponseStructure()
    data = CreateShortenedUrlSerializer(data=request.data)
    if data.is_valid():
        url_obj = data.save(user=request.user)
        serialized = ShortenedUrlSerializer(url_obj)
        r.status = True
        r.data.append(serialized.data)
        return Response(r.object(), status=status.HTTP_200_OK)
    r.message = data.errors
    return Response(r.object(), status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllUrls(request) -> Response:
    r = StandardResponseStructure()
    urls = StoredUrls.objects.filter(user=request.user)
    serialized = ShortenedUrlSerializer(urls, many=True)
    r.status = True
    r.data = serialized.data
    return Response(r.object(), status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def editShortenedUrl(request, pk) -> Response:
    r = StandardResponseStructure()
    try:
        instance = StoredUrls.objects.get(pk=pk)
        if not instance.user == request.user:
            raise ObjectDoesNotExist
    except ObjectDoesNotExist:
        r.message = 'URL not found or user not authorized'
        return Response(r.object(), status=status.HTTP_200_OK)
    data = CreateShortenedUrlSerializer(instance, data=request.data, partial=True)
    if data.is_valid():
        obj = data.save()
        serialized = ShortenedUrlSerializer(obj)
        r.data.append(serialized.data)
        r.status = True
        return Response(r.object(), status=status.HTTP_200_OK)
    r.message = data.errors
    return Response(r.object(), status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def deleteShortenedUrl(request, pk) -> Response:
    r = StandardResponseStructure()
    try:
        instance = StoredUrls.objects.get(pk=pk)
        if not instance.user == request.user:
            raise ObjectDoesNotExist
    except ObjectDoesNotExist:
        r.message = 'URL not found or user not authorized'
        return Response(r.object(), status=status.HTTP_200_OK)
    instance.delete()
    r.status = True
    return Response(r.object(), status=status.HTTP_200_OK)


def redirectToUrl(request, shortened_url):
    try:
        instance = StoredUrls.objects.get(shortened_url=shortened_url)
        if instance.expiry_time < timezone.now():
            return HttpResponse("Link Expired!")
        instance.increment_visits()
        return HttpResponsePermanentRedirect(instance.redirect_url)
    except ObjectDoesNotExist:
        raise Http404
    except:
        return HttpResponseServerError("Something went wrong!")
