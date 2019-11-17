from django.urls import path
from django.conf.urls import url, include
from . import views
from rest_framework import serializers, viewsets, routers
from django.urls import path, re_path



router = routers.DefaultRouter()
# router.register(r'passwords', views.PasswordViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^health_check/', include('health_check.urls')),
    path(r'get_word',views.get_word),
]