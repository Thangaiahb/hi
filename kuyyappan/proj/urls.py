"""
URL configuration for proj project.

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
from myapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='ho'),
    path('contact/',views.con,name='co'),
    path('about/',views.ab,name='ao'),
    path('dele/<int:id>',views.dele),
    path('up/<int:id>',views.upe),
    path('register/',views.regi,name='reg'),
    path('log-in/',auto.LoginView.as_view(template_name='log.html'),name='lo'),
    path('user/',views.dash,name='da'),
path("logou/", auto.LogoutView.as_view(template_name="log.html"), name='loout'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)