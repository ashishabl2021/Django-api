from django.urls import path
from backend import serializers


urlpatterns = [
    path('getnames/', serializers.GetNames),
    path('box/<int:box_id>/', serializers.box_detail),
]