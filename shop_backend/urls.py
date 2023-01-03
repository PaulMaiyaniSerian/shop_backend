"""shop_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="Shop API",
      default_version='v1',
      description="Backend Api for Shop Api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="paulmaiyanideveloper@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# sentry debug
from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0



urlpatterns = [
    path('sentry-debug/', trigger_error),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls"), name="accounts"),
    path('core/', include("core.urls"), name="core"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)