"""rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from authusersapp.views import BaseUsersViewSet
from moderationapp.views import UserModViewSet, TransportModViewSet, OrderModViewSet
from orderapp.views import OrderView, MyTransportOrderView
from reviewapp.views import ReviewViewSet

from transportapp.views import TransportViewSet, TransportTypeViewSet, ManufacturerViewSet, MyTransportViewSet

router = DefaultRouter()
router.register('clients', BaseUsersViewSet)
router.register('transports', TransportViewSet)
router.register('transport_type', TransportTypeViewSet)
router.register('manufacturer', ManufacturerViewSet)
router.register('orders', OrderView)
router.register('orders-from-me', MyTransportOrderView, basename='orders-from-me')
router.register('reviews', ReviewViewSet)
router.register('mytransport', MyTransportViewSet, basename='mytransport')

moder_router = DefaultRouter()
moder_router.register('users', UserModViewSet, basename='mod_users')
moder_router.register('transports', TransportModViewSet, basename='mod_transport')
moder_router.register('orders', OrderModViewSet, basename='mod_orders')

schema_view = get_schema_view(
    openapi.Info(
        title="Bike&Scooter",
        description='Documentation for "Bike&Scooter". Bicycle rental service.',
        default_version='0.0.1',
        contact=openapi.Contact(email='scooterbikeshare@gmail.com'),
        license=openapi.License(name='MIT License')
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('api/', include(router.urls)),
    path('moderation/', include(moder_router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # urls.py-проекта адреса для авторизации DRF.
    path('auth/', include('djoser.urls')),  # путь для работы регистрации и авторизации
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # путь для работы с токенами

    path('change-status/', include('orderapp.urls', namespace='change_status')),
    # два варианта документации. оставим один.
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
