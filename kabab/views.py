from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import  DjangoModelPermissions
from rest_framework import viewsets
from .models import *

class MenyuPageNumberPaginations(PageNumberPagination):
    page_size = 3


class MenyuViewSet(viewsets.ModelViewSet):
    queryset = Menyu.objects.all()
    serializer_class = MenyuSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [ DjangoModelPermissions]
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name','price']
    ordering = ['price']
    search_fields = ['^name']
    filterset_fields = ['name',]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer