"""
URL configuration for proyectoUTDdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path, include, re_path # type: ignore

from django.conf import settings #Para debug false # type: ignore
from django.conf.urls.static import static # type: ignore


from django.views.static import serve  # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
]

if not settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]


# SE DEBE HACER collectsatics antes de correr els server para que esto funcione y debe estar el debug en FALSE

handler404 = 'mainapp.views.error404_2'