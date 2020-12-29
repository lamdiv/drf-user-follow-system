from django.urls import path,include, re_path
from .views import UserContactViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'followings', UserContactViewset,basename="model")

urlpatterns = [
  path('',include('djoser.urls')),
  path('',include('djoser.urls.jwt')),
  path('', include(router.urls)),
]
