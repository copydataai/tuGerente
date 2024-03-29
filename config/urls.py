"""config URL Configuration

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
from django.urls import path
from django.urls.conf import include

# DRF
from rest_framework.routers import DefaultRouter
from bill.views import BillViewSet

# DRF-spectacular
from drf_spectacular.views import SpectacularAPIView

# Views
from clients.views import ClientSignUp, ClientLogin
from reserves.views import ReserverViewSet
from rooms.views import RoomViewSet

router = DefaultRouter()

router.register('reserves', ReserverViewSet)
router.register('rooms', RoomViewSet)
router.register('bills', BillViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/signup/', ClientSignUp.as_view()),
    path('clients/login/', ClientLogin.as_view()),
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view())
]
