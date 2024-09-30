"""
URL configuration for tourist-spots project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from core.api.viewsets import TouristSpotViewSet, LoginView
from attractions.api.viewsets import AttractionViewSet
from address.api.viewsets import AddressViewSet
from comments.api.viewsets import CommentViewSet
from ratings.api.viewsets import RatingViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'tourist-spots', TouristSpotViewSet, basename='tourist-spots')
router.register(r'attractions', AttractionViewSet, basename='attractions')
router.register(r'address', AddressViewSet, basename='address')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'ratings', RatingViewSet, basename='ratings')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/login/', LoginView.as_view(), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
