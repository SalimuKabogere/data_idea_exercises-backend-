# from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Activity
from .serializers import ActivitySerializer

# Create your views here.

# class ActivityViewSet(viewsets.ModelViewSet):
#     """
#     API endpoints that allows activities to  be viewed or edited
#     """
#     queryset = Activity.objects.all().order_by('-created')
#     serializer_class = ActivitySerializer

class ActivityListCreate(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer