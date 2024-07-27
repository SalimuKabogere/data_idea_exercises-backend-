from django.urls import path
from .views import ActivityListCreate, ActivityUpdateDelete

urlpatterns = [
    path('activities/', ActivityListCreate.as_view(), name='activity-list-create'),
    path('activities/<int:pk>/', ActivityUpdateDelete.as_view(), name='activity-update-delete'),
]
