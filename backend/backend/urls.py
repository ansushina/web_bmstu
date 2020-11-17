"""backend URL Configuration

The `urlpatterns` list routes URLs to viewssss. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function viewssss
    1. Add an import:  from my_app import viewssss
    2. Add a URL to urlpatterns:  path('', viewssss.home, name='home')
Class-based viewssss
    1. Add an import:  from other_app.viewssss import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from backend import settings

schema_view = get_schema_view(
    openapi.Info(
        title="MoviesToWatch API",
        default_version='v1',
        description="API for service MoviesToWatch",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="nastya.sushina@yandex.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('', include("app.urls"))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
