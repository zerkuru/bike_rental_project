from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orderapp.views import IsAuthenticatedUser, IsAdmin
from reviewapp.models import Review
from reviewapp.serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    model = Review
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticatedUser | IsAdmin]
    filterset_fields = ['score']
    http_method_names = ['get', 'patch', 'head', 'options', 'trace', 'delete', 'post']

